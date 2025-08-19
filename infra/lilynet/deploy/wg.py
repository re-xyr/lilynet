from pyinfra.operations import apk, files, openrc
from pyinfra.context import host
from lilynet.schema import Wg
from lilynet.view import get_view

view = get_view(host)

apk.packages(packages=["wireguard-tools"])

for peer in host.loop(view.local.dn42_peers):
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

for upstream in host.loop(view.local.upstreams):
    if not isinstance(upstream.tunnel, Wg):
        continue  # Skip non-Wg tunnels

    upstream_result = files.template(
        src="lilynet/config/wireguard/upstream.conf.j2",
        dest=f"/etc/wireguard/wgu{upstream.asn}.conf",
        # j2 variables
        local=view.local,
        local_secrets=view.local_secrets,
        upstream=upstream,
    )
    files.link(
        path=f"/etc/init.d/wg-quick.wgu{upstream.asn}",
        target="/etc/init.d/wg-quick",
    )
    openrc.service(
        service=f"wg-quick.wgu{upstream.asn}",
        enabled=True,
        reloaded=upstream_result.changed,
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
