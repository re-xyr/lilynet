from pyinfra.operations import apk, files, openrc

apk.packages(packages=["bind"])

files.directory(
    path="/var/named",
    user="named",
    group="named",
    mode="0755",
)

named_result = files.sync(
    src="lilynet/config/bind",
    dest="/etc/bind",
)

openrc.service(service="named", enabled=True, reloaded=named_result.changed)
