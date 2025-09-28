from lilynet.schema import (
    Interface,
    Node,
    Dn42Peer,
    Wg,
    WgTemplate,
    Host,
    Router,
    Upstream,
    Direct,
)
from lilynet.data.secrets import global_secrets

sjc1: Node = Node(
    name="sjc1",
    underlay=Host(
        hostname="sjc1.node.dayli.ly",
        ipv4="149.28.212.242",
        ipv6="2001:19f0:ac00:495b:5400:05ff:fe69:c8b7",
    ),
    wg=WgTemplate(
        local_port=30002,
        peer_pubkey="yOt9PIXDa4pzAE+XMzDv7J+CYO2qf53fnF9MvLy4iQ8=",
        peer_ll_ipv6="fe80::2",
    ),
    clearnet=Router(
        host=Host(
            hostname="sjc1.daylily.network",
            ipv6="2620:d7:6002::1",
            ipv4="23.142.212.253",
        ),
        ipv4s=["23.142.212.1"],
        ipv6s=["2620:d7:6000::1"],
        ipv4_prefixes=["23.142.212.0/24"],
        ipv6_prefixes=[
            "2620:d7:6000::/48",
            "2620:d7:6002::/48",
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
            ipv4="172.21.89.66",
            ipv6="fd11:4514:1919:2::1",
        ),
        ipv4_prefixes=["172.21.89.64/27"],
        ipv6_prefixes=["fd11:4514:1919::/48"],
    ),
    dn42_peers=[
        Dn42Peer(
            name="routedbits",
            asn=4242420207,
            underlay=Host(hostname="router.scl1.routedbits.com"),
            wg=Wg(
                peer_pubkey="AByV6Tu2gkb+cDzNKcsVM2ntLCrnL4IA89nKSVTfXWc=",
                peer_port=51919,
                peer=Host(ipv6="fe80::0207", ipv4="172.20.19.90"),
                local_port=40207,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="prefixlabs",
            asn=4242421240,
            underlay=Host(hostname="us-03.prefixlabs.net"),
            wg=Wg(
                peer_pubkey="oNabDMpFKum4CRbvPcwVE0Y4QsAfH0Sh439dfQYhnkQ=",
                peer_port=21919,
                peer=Host(ipv6="fe80::1240:4", ipv4="172.20.209.13"),
                local_port=41240,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="tech9",
            asn=4242421588,
            underlay=Host(hostname="us-phx03.dn42.tech9.io"),
            wg=Wg(
                peer_pubkey="bRkI8aGjwwgm1I6WeqsfL6jrxu72ifs3xSaTLCY22mw=",
                peer_port=59745,
                peer=Host(ipv6="fe80::1588", ipv4="172.23.220.178"),
                local_port=41588,
                local=Interface(ipv6="fe80::0100", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="duststars",
            asn=4242421771,
            underlay=Host(hostname="lax1-dn42.exploro.one"),
            wg=Wg(
                peer_pubkey="6cf3xLB8SB4R2xvU+I9H1rwy3LW3WSh06oK1n0HE/nA=",
                peer_port=32613,
                peer=Host(ipv6="fe80::9689:4c1b:770d:b0b7"),
                local_port=41771,
                local=Interface(ipv6="fe80::1771"),
            ),
        ),
        Dn42Peer(
            name="ideon",
            asn=4242422189,
            underlay=Host(hostname="us-lax.dn42.kuu.moe"),
            wg=Wg(
                peer_pubkey="DIw4TKAQelurK10Sh1qE6IiDKTqL1yciI5ItwBgcHFA=",
                peer_port=52320,
                peer=Host(ipv6="fe80::2189:ef", ipv4="172.23.91.114"),
                local_port=42189,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="amemiya",
            asn=4242422464,
            underlay=Host(hostname="las.dneo.moeternet.com"),
            wg=Wg(
                peer_pubkey="viR4CoaJTBHROo/Bgbb27hQ2ttr8AbByGY/yOz3D3GY=",
                peer_port=21919,
                peer=Host(ipv6="fe80::2464"),
                local_port=42464,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
        Dn42Peer(
            name="lare",
            asn=4242423035,
            underlay=Host(hostname="usw1.dn42.lare.cc"),
            wg=Wg(
                peer_pubkey="Qd2XCotubH4QrQIdTZjYG4tFs57DqN7jawO9vGz+XWM=",
                peer_port=21919,
                peer=Host(ipv6="fe80::3035:132"),
                local_port=43035,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
        Dn42Peer(
            name="kioubit",
            asn=4242423914,
            underlay=Host(hostname="us3.g-load.eu"),
            wg=Wg(
                peer_pubkey="sLbzTRr2gfLFb24NPzDOpy8j09Y6zI+a7NkeVMdVSR8=",
                peer_port=21919,
                peer=Host(ipv6="fe80::ade0", ipv4="172.20.53.103"),
                local_port=43914,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="cowgl",
            asn=4242423999,
            underlay=Host(hostname="lax.node.cowgl.xyz"),
            wg=Wg(
                peer_pubkey="jhOukGNAKHI8Ivn8uI1TS25n5ho/rVlKFfenGmwCVlg=",
                peer_port=31919,
                peer=Host(ipv6="fe80::2:3999", ipv4="172.22.144.66"),
                local_port=43999,
                local=Interface(ipv6="fe80::1919", ipv4="172.21.89.66"),
            ),
        ),
        Dn42Peer(
            name="iyoroy",
            asn=4242422024,
            underlay=Host(hostname="ipv4.lax-us.ecs.iyoroy-infra.top"),
            wg=Wg(
                peer_pubkey="As0rZo5b9Bwt4loPGl6iSdtOqkd2p6ExK/Xyoy9OmTU=",
                peer_port=21919,
                peer=Host(ipv6="fe80::2024"),
                local_port=42024,
                local=Interface(ipv6="fe80::1919"),
            ),
        ),
    ],
)
