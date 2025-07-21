from pyinfra.operations import files, openrc
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

# Set up dummy iface
dummy_iface_result = files.template(
    src="lilynet/config/local.d/dummy-iface.start.j2",
    dest="/etc/local.d/dummy-iface.start",
    mode="0755",
    # j2 variables
    local=view.local,
)

openrc.service(
    service="local",
    enabled=True,
    restarted=dummy_iface_result.changed,
)
