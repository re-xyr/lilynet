from lilynet.schema import Node, Host, WgTemplate

nrt1: Node = Node(
    name="nrt1",
    underlay=Host(
        hostname="nrt1.node.dayli.ly",
        ipv4="198.13.50.205",
        ipv6="2001:19f0:7002:10ad:5400:05ff:fe8b:d267",
    ),
    wg=WgTemplate(
        local_port=30003,
        peer_pubkey="LqU2X19XCcG36bI2bEHm68B6GNWDfFfpQnoirtD8X0c=",
        peer_ll_ipv6="fe80::3",
    ),
    clearnet=Host(
        ipv6="2620:d7:6000:3::1",
        hostname="nrt1.daylily.network",
    ),
    dn42=Host(
        ipv4="172.21.89.67",
        ipv6="fd11:4514:1919:3::1",
    ),
)
