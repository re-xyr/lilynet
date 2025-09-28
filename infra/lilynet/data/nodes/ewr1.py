from lilynet.schema import (
    Interface,
    Node,
    Dn42Peer,
    Host,
    Wg,
    WgTemplate,
    Router,
    Upstream,
    Direct,
)
from lilynet.data.secrets import global_secrets

ewr1: Node = Node(
    name="ewr1",
    underlay=Host(
        hostname="ewr1.node.dayli.ly",
        ipv4="207.148.28.92",
        ipv6="2001:19f0:1000:9985:5400:05ff:fe69:4b94",
    ),
    wg=WgTemplate(
        local_port=30001,
        peer_pubkey="F6YGAEiF7VLd2r2DW/jX7vC8235b4DJf6HD29gRi6gg=",
        peer_ll_ipv6="fe80::1",
    ),
    clearnet=Router(
        host=Host(
            hostname="ewr1.daylily.network",
            ipv6="2620:d7:6001::1",
            ipv4="23.142.212.254",
        ),
        ipv4s=["23.142.212.1"],
        ipv6s=["2620:d7:6000::1"],
        ipv4_prefixes=["23.142.212.0/24"],
        ipv6_prefixes=[
            "2620:d7:6000::/48",
            "2620:d7:6001::/48",
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
            ipv4="172.21.89.65",
            ipv6="fd11:4514:1919:1::1",
        ),
        ipv4_prefixes=["172.21.89.64/27"],
        ipv6_prefixes=["fd11:4514:1919::/48"],
    ),
    dn42_peers=[
        Dn42Peer(
            name="darkpoint",
            asn=4242420150,
            underlay=Host(hostname="iad.darkpoint.xyz"),
            wg=Wg(
                peer_pubkey="1o0XfQvBM1gqknqzfuOnVmf2RjRTHuyMZYNipSSb2TQ=",
                peer_port=21919,
                peer=Host(ipv6="fe80::150"),
                local_port=40150,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
        Dn42Peer(
            name="routedbits",
            asn=4242420207,
            underlay=Host(hostname="router.ewr1.routedbits.com"),
            wg=Wg(
                peer_pubkey="Yelo0BWe4ggUQ1jTKmC1Tq2Tqg1jyKiVU5xz+qY0yU0=",
                peer_port=51919,
                peer=Host(ipv6="fe80::0207", ipv4="172.20.19.69"),
                local_port=40207,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="prefixlabs",
            asn=4242421240,
            underlay=Host(hostname="us-01.prefixlabs.net"),
            wg=Wg(
                peer_pubkey="uRYzFGi+/B6pD0FR2SW3G/OzC5LPJXePNIt0s+nJfW0=",
                peer_port=21919,
                peer=Host(ipv6="fe80::1240:2", ipv4="172.20.209.11"),
                local_port=41240,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="tech9",
            asn=4242421588,
            underlay=Host(hostname="us-chi01.dn42.tech9.io"),
            wg=Wg(
                peer_pubkey="0kb8ffMcbx8oXZ3Ii5khOuCzmRqM2Cy0IslmrWtRGSk=",
                peer_port=53146,
                peer=Host(ipv6="fe80::1588", ipv4="172.20.53.98"),
                local_port=41588,
                local=Interface(ipv6="fe80::0100", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="duststars",
            asn=4242421771,
            underlay=Host(hostname="nyc1.exploro.one"),
            wg=Wg(
                peer_pubkey="dULQpv0J8inucdpbNepUl1X9QETe/EQqfLSlkkxeikI=",
                peer_port=40005,
                peer=Host(ipv6="fe80::e1f1:2bb1:b5c5:37d"),
                local_port=41771,
                local=Interface(ipv6="fe80::1771"),
            ),
        ),
        Dn42Peer(
            name="potat0",
            asn=4242421816,
            underlay=Host(hostname="las.node.potat0.cc"),
            wg=Wg(
                peer_pubkey="LUwqKS6QrCPv510Pwt1eAIiHACYDsbMjrkrbGTJfviU=",
                peer_port=21919,
                peer=Host(ipv6="fe80::1816", ipv4="172.23.246.3"),
                local_port=41816,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="ideon",
            asn=4242422189,
            underlay=Host(hostname="us-sjc.dn42.kuu.moe"),
            wg=Wg(
                peer_pubkey="Sz0UhewjDk2yRKI0QL9rB+5daWpXFVlbbz9cLfVVLn4=",
                peer_port=52644,
                peer=Host(ipv6="fe80::2189:e8", ipv4="172.23.91.117"),
                local_port=42189,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="amemiya",
            asn=4242422464,
            underlay=Host(hostname="nyc.dneo.moeternet.com"),
            wg=Wg(
                peer_pubkey="MLVJrwrph6d0VqrAq8/rkhbkG+mrQNytqmwrNgk2qFs=",
                peer_port=21919,
                peer=Host(ipv6="fe80::2464"),
                local_port=42464,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
        Dn42Peer(
            name="lare",
            asn=4242423035,
            underlay=Host(hostname="use2.dn42.lare.cc"),
            wg=Wg(
                peer_pubkey="AREskFoxP2cd6DXoJ7druDsiWKX+8TwrkQqfi4JxRRw=",
                peer_port=21919,
                peer=Host(ipv6="fe80::3035:137"),
                local_port=43035,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
        Dn42Peer(
            name="kioubit",
            asn=4242423914,
            underlay=Host(hostname="us2.g-load.eu"),
            wg=Wg(
                peer_pubkey="6Cylr9h1xFduAO+5nyXhFI1XJ0+Sw9jCpCDvcqErF1s=",
                peer_port=21919,
                peer=Host(ipv6="fe80::ade0", ipv4="172.20.16.139"),
                local_port=43914,
                local=Interface(ipv6="fe80::ade1", ipv4="172.21.89.65"),
            ),
        ),
        Dn42Peer(
            name="cowgl",
            asn=4242423999,
            underlay=Host(hostname="yyz.node.cowgl.xyz"),
            wg=Wg(
                peer_pubkey="XGIBvqoUOgb8IiLIWtO9JVNZc4SEpEAM1eWh26MtoRE=",
                peer_port=31919,
                peer=Host(ipv6="fe80::5:3999", ipv4="172.22.144.69"),
                local_port=43999,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.65"),
            ),
        ),
    ],
)
