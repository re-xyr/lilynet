from lilynet.schema import Node
from lilynet.data.downstreams import workstation

nrt1: Node = Node(
    name="nrt1",
    hostname="nrt1.node.dayli.ly",
    public_key="LqU2X19XCcG36bI2bEHm68B6GNWDfFfpQnoirtD8X0c=",
    ipv4="172.21.89.67",
    ipv6="fd11:4514:1919:3::1",
    clearnet_ipv4="198.13.50.205",
    clearnet_ipv6="2620:d7:6000:3::1",
    stable_port=30003,
    stable_link_ipv6="fe80::3",
    peers=[],
    downstreams=[workstation],
)
