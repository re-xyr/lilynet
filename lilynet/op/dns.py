from pyinfra import local
from pyinfra.operations import apt, files, systemd

local.include("lilynet/op/ip.py")

apt.packages(packages=["bind9"])

files.directory(
    path="/var/named",
    user="bind",
    group="bind",
    mode="0755",
)

named_result = files.sync(
    src="lilynet/config/bind",
    dest="/etc/bind",
)

systemd.service(service="named", enabled=True, reloaded=named_result.changed)
