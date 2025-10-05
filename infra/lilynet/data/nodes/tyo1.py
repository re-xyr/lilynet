from lilynet.schema import Direct, Node, Host, Upstream, WgTemplate, Router
from lilynet.data.secrets import global_secrets

tyo1: Node = Node(
    name="tyo1",
    underlay=Host(
        hostname="tyo1.node.dayli.ly",
        ipv4="198.13.50.205",
        ipv6="2001:19f0:7002:10ad:5400:05ff:fe8b:d267",
    ),
    wg=WgTemplate(
        local_port=30003,
        peer_pubkey="LqU2X19XCcG36bI2bEHm68B6GNWDfFfpQnoirtD8X0c=",
        peer_ll_ipv6="fe80::3",
    ),
    clearnet=Router(
        host=Host(
            hostname="tyo1.daylily.network",
            ipv6="2620:d7:6003::1",
            ipv4="23.142.212.252",
        ),
        ipv4s=["23.142.212.1"],
        ipv6s=["2620:d7:6000::1"],
        ipv4_prefixes=["23.142.212.0/24"],
        ipv6_prefixes=[
            "2620:d7:6000::/48",
            "2620:d7:6003::/48",
        ],
    ),
    upstreams=[
        Upstream(
            name="vultr",
            asn=64515,
            multihop=True,
            underlay=Host(),  # Direct link on eth0
            tunnel=Direct(
                peer=Host(ipv4="169.254.169.254", ipv6="2001:19f0:ffff::1"),
            ),
            password=global_secrets["vultr_bgp_password"],
        ),
    ],
    dn42=Router(
        host=Host(
            ipv4="172.21.89.67",
            ipv6="fd11:4514:1919:3::1",
        ),
        ipv4_prefixes=["172.21.89.64/27"],
        ipv6_prefixes=["fd11:4514:1919::/48"],
    ),
)
