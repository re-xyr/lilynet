from pyinfra import local
from pyinfra.operations import apt, files, systemd
from pyinfra.context import host
from lilynet.view import get_view

local.include("lilynet/op/wg.py")

view = get_view(host)

apt.packages(packages=["babeld"])

babeld_result = files.template(
    src="lilynet/config/babel/babeld.conf.j2",
    dest="/etc/babeld.conf",
    # j2 variables
    local=view.local,
    network=view.network,
)

systemd.service(
    service="babeld",
    enabled=True,
    restarted=babeld_result.changed,
)
