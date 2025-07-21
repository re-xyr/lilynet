from pyinfra.operations import apk, files, openrc
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apk.packages(packages=["tor"])

torrc_result = files.template(
    src="lilynet/config/tor/torrc.j2",
    dest="/etc/tor/torrc",
    # j2 variables
    local=view.local,
)
openrc.service(
    service="tor",
    enabled=True,
    reloaded=torrc_result.changed,
)
