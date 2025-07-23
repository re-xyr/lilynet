from pyinfra.operations import files, openrc
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

files.put(
    src="lilynet/config/iproute2/rt_tables",
    dest="/etc/iproute2/rt_tables",
)

routing_policy_result = files.put(
    src="lilynet/config/local.d/routing-policy.start",
    dest="/etc/local.d/routing-policy.start",
    mode="0755",
)

openrc.service(
    service="local",
    enabled=True,
    restarted=routing_policy_result.changed,
)
