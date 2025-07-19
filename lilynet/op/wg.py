from pyinfra import local
from pyinfra.operations import apt, files, systemd
from pyinfra.context import host
from lilynet.view import get_view

local.include("lilynet/op/ip.py")

view = get_view(host)

apt.packages(packages=["wireguard-tools"])

for peer in host.loop(view.local.peers):
    peer_result = files.template(
        src="lilynet/config/wireguard/peer.conf.j2",
        dest=f"/etc/wireguard/wg{peer.asn}.conf",
        # j2 variables
        local=view.local,
        local_secrets=view.local_secrets,
        peer=peer,
    )
    systemd.service(
        service=f"wg-quick@wg{peer.asn}",
        enabled=True,
        restarted=peer_result.changed,
    )

for node in host.loop(view.network):
    node_result = files.template(
        src="lilynet/config/wireguard/network.conf.j2",
        dest=f"/etc/wireguard/wg{node.name}.conf",
        # j2 variables
        local=view.local,
        local_secrets=view.local_secrets,
        node=node,
    )
    systemd.service(
        service=f"wg-quick@wg{node.name}",
        enabled=True,
        restarted=node_result.changed,
    )

router_result = files.template(
    src="lilynet/config/wireguard/router.conf.j2",
    dest="/etc/wireguard/wgrouter.conf",
    # j2 variables
    local=view.local,
    local_secrets=view.local_secrets,
)
systemd.service(
    service="wg-quick@wgrouter",
    enabled=True,
    restarted=router_result.changed,
)
