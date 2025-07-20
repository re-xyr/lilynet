from pyinfra.operations import apt, files, systemd, server
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apt.packages(packages=["bird2"])

# Timed dn42 ROA import

dn42_roa_service_result = files.put(
    src="lilynet/config/systemd/dn42-roa.service",
    dest="/etc/systemd/system/dn42-roa.service",
)
dn42_roa_timer_result = files.put(
    src="lilynet/config/systemd/dn42-roa.timer",
    dest="/etc/systemd/system/dn42-roa.timer",
)

should_reload = dn42_roa_service_result.changed or dn42_roa_timer_result.changed
systemd.service(
    service="dn42-roa.timer",
    enabled=True,
    reloaded=should_reload,
    restarted=should_reload,
)

# Enable IP forwarding in sysctl

server.sysctl(key="net.ipv4.conf.default.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.conf.all.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.ip_forward", value="1", persist=True)
server.sysctl(key="net.ipv6.conf.all.forwarding", value="1", persist=True)

# Set up BIRD

systemd.service(service="bird", enabled=True)
bird_conf_result = files.template(
    src="lilynet/config/bird/bird.conf.j2",
    dest="/etc/bird/bird.conf",
    # j2 variables
    local=view.local,
    network=view.network,
    global_secrets=view.global_secrets,
)
if bird_conf_result.changed:
    server.shell(
        name="Restart BIRD",
        commands=["birdc configure"],
    )
