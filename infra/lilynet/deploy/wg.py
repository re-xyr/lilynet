from pyinfra.operations import apk, files, openrc
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

apk.packages(packages=["wireguard-tools"])

for peer in host.loop(view.local.peers):
    peer_result = files.template(
        src="lilynet/config/wireguard/peer.conf.j2",
        dest=f"/etc/wireguard/wgd{peer.asn}.conf",
        # j2 variables
        local=view.local,
        local_secrets=view.local_secrets,
        peer=peer,
    )
    files.link(
        path=f"/etc/init.d/wg-quick.wgd{peer.asn}",
        target="/etc/init.d/wg-quick",
    )
    openrc.service(
        service=f"wg-quick.wgd{peer.asn}",
        enabled=True,
        reloaded=peer_result.changed,
    )

for node in host.loop(view.network):
    node_result = files.template(
        src="lilynet/config/wireguard/network.conf.j2",
        dest=f"/etc/wireguard/wgn{node.name}.conf",
        # j2 variables
        local=view.local,
        local_secrets=view.local_secrets,
        node=node,
    )
    files.link(
        path=f"/etc/init.d/wg-quick.wgn{node.name}",
        target="/etc/init.d/wg-quick",
    )
    openrc.service(
        service=f"wg-quick.wgn{node.name}",
        enabled=True,
        reloaded=node_result.changed,
    )

router_result = files.template(
    src="lilynet/config/wireguard/router.conf.j2",
    dest="/etc/wireguard/wgrouter.conf",
    # j2 variables
    local=view.local,
    local_secrets=view.local_secrets,
)
files.link(
    path="/etc/init.d/wg-quick.wgrouter",
    target="/etc/init.d/wg-quick",
)
openrc.service(
    service="wg-quick.wgrouter",
    enabled=True,
    reloaded=router_result.changed,
)
