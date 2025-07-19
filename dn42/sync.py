from pyinfra.operations import apt, files, systemd, server
from pyinfra.context import host
from dn42.data.directory import nodes as directory
from dn42.data.secrets import nodes as secrets

# Install required packages

apt.packages(packages=["babeld", "bird2", "dnsmasq", "nftables", "wireguard-tools"])

# Timed dn42 ROA import

dn42_roa_service_result = files.put(
    src="dn42/config/systemd/dn42-roa.service",
    dest="/etc/systemd/system/dn42-roa.service",
)
dn42_roa_timer_result = files.put(
    src="dn42/config/systemd/dn42-roa.timer",
    dest="/etc/systemd/system/dn42-roa.timer",
)

should_reload = dn42_roa_service_result.changed or dn42_roa_timer_result.changed
systemd.service(
    service="dn42-roa.timer",
    enabled=True,
    reloaded=should_reload,
    restarted=should_reload,
)

# Set up dnsmasq

dnsmasq_result = files.put(
    src="dn42/config/dnsmasq.conf",
    dest="/etc/dnsmasq.conf",
)
systemd.service(service="dnsmasq", enabled=True, restarted=dnsmasq_result.changed)

# Set up nftables

nftables_result = files.put(
    src="dn42/config/nftables.conf",
    dest="/etc/nftables.conf",
)
systemd.service(service="nftables", enabled=True, restarted=nftables_result.changed)

# Enable IP forwarding in sysctl

server.sysctl(key="net.ipv4.conf.default.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.conf.all.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.ip_forward", value="1", persist=True)
server.sysctl(key="net.ipv6.conf.all.forwarding", value="1", persist=True)

local = directory.get(host.name)
local_secrets = secrets.get(host.name)
if local is None or local_secrets is None:
    raise ValueError(f"No entry found for host {host.name} in directory.")
network = [node for node in directory.values() if node.name != local.name]

# Set up dummy iface

dummy_iface_result = files.template(
    src="dn42/config/dummy-iface.sh.j2",
    dest="/usr/local/bin/dummy-iface.sh",
    mode="0755",
    # j2 variables
    local=local,
)

if dummy_iface_result.changed:
    server.shell(
        name="Set up dummy interface",
        commands=["/usr/local/bin/dummy-iface.sh"],
    )

# Set up WireGuard

for peer in host.loop(local.peers):
    peer_result = files.template(
        src="dn42/config/wireguard/peer.conf.j2",
        dest=f"/etc/wireguard/wg{peer.asn}.conf",
        # j2 variables
        local=local,
        local_secrets=local_secrets,
        peer=peer,
    )
    systemd.service(
        service=f"wg-quick@wg{peer.asn}",
        enabled=True,
        restarted=peer_result.changed,
    )

for node in host.loop(directory.values()):
    if node.hostname == host.name:
        continue
    node_result = files.template(
        src="dn42/config/wireguard/network.conf.j2",
        dest=f"/etc/wireguard/wg{node.name}.conf",
        # j2 variables
        local=local,
        local_secrets=local_secrets,
        node=node,
    )
    systemd.service(
        service=f"wg-quick@wg{node.name}",
        enabled=True,
        restarted=node_result.changed,
    )

router_result = files.template(
    src="dn42/config/wireguard/router.conf.j2",
    dest="/etc/wireguard/wgrouter.conf",
    # j2 variables
    local=local,
    local_secrets=local_secrets,
)
systemd.service(
    service="wg-quick@wgrouter",
    enabled=True,
    restarted=router_result.changed,
)

# Set up babeld

babeld_result = files.template(
    src="dn42/config/babel/babeld.conf.j2",
    dest="/etc/babeld.conf",
    # j2 variables
    local=local,
    network=network,
)
systemd.service(
    service="babeld",
    enabled=True,
    restarted=babeld_result.changed,
)

# Set up BIRD

systemd.service(service="bird", running=True, enabled=True)
bird_conf_result = files.template(
    src="dn42/config/bird/bird.conf.j2",
    dest="/etc/bird/bird.conf",
    # j2 variables
    local=local,
    network=network,
    local_secrets=local_secrets,
)
if bird_conf_result.changed:
    server.shell(
        name="Restart BIRD",
        commands=["birdc configure"],
    )
