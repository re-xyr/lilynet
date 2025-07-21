from pyinfra.operations import apk, files, openrc
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apk.packages(packages=["babeld"])

babeld_result = files.template(
    src="lilynet/config/babeld.conf.j2",
    dest="/etc/babeld.conf",
    # j2 variables
    local=view.local,
    network=view.network,
)

openrc.service(
    service="babeld",
    enabled=True,
    restarted=babeld_result.changed,
)
