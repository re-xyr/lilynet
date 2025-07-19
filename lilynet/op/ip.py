from pyinfra.operations import apt, files, systemd
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apt.packages(packages=["nftables"])

nftables_result = files.put(
    src="lilynet/config/nftables.conf",
    dest="/etc/nftables.conf",
)
systemd.service(service="nftables", enabled=True, restarted=nftables_result.changed)

# Set up dummy iface
dummy_iface_result = files.template(
    src="lilynet/config/dummy-iface.sh.j2",
    dest="/usr/local/bin/dummy-iface.sh",
    mode="0755",
    # j2 variables
    local=view.local,
)
dummy_iface_service_result = files.put(
    src="lilynet/config/systemd/dummy-iface.service",
    dest="/etc/systemd/system/dummy-iface.service",
)
systemd.service(
    service="dummy-iface.service",
    enabled=True,
    reloaded=dummy_iface_service_result.changed,
    restarted=dummy_iface_result.changed or dummy_iface_service_result.changed,
)
