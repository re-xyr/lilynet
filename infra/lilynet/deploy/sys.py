from pyinfra.operations import files, openrc, server
from pyinfra.context import host

# Set hostname

server.hostname(hostname=host.name)

# Disable password authentication for SSH

files.put(
    src="lilynet/config/cloud/cloud.cfg.d/99-no-pwauth.cfg",
    dest="/etc/cloud/cloud.cfg.d/99-no-pwauth.cfg",
)

# Enable IP forwarding in sysctl

server.sysctl(key="net.ipv4.conf.default.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.conf.all.rp_filter", value="0", persist=True)
server.sysctl(key="net.ipv4.ip_forward", value="1", persist=True)
server.sysctl(key="net.ipv6.conf.all.forwarding", value="1", persist=True)

# Reboot every week

files.put(
    src="lilynet/config/periodic/weekly/restart.sh",
    dest="/etc/periodic/weekly/restart.sh",
    mode="0755",
)
openrc.service(
    service="crond",
    enabled=True,
)
