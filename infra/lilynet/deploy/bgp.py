from pyinfra.operations import apk, files, openrc, server
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apk.packages(packages=["bird2"])

# Timed dn42 ROA import

roa_timer_result = files.put(
    src="lilynet/config/periodic/15min/dn42-roa.sh",
    dest="/etc/periodic/15min/dn42-roa.sh",
    mode="0755",
)
openrc.service(
    service="crond",
    enabled=True,
)
server.shell(
    commands=["/etc/periodic/15min/dn42-roa.sh"],
    _if=roa_timer_result.did_change,
)

# Set up BIRD

bird_conf_result = files.template(
    src="lilynet/config/bird.conf.j2",
    dest="/etc/bird.conf",
    # j2 variables
    local=view.local,
    network=view.network,
    global_secrets=view.global_secrets,
)
openrc.service(
    service="bird",
    enabled=True,
    restarted=bird_conf_result.changed,
)
