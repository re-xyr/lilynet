from lilynet.schema import Node
from lilynet.data.nodes.ewr1 import ewr1
from lilynet.data.nodes.nrt1 import nrt1
from lilynet.data.nodes.sjc1 import sjc1

nodes: dict[str, Node] = {
    "ewr1.node.dayli.ly": ewr1,
    "nrt1.node.dayli.ly": nrt1,
    "sjc1.node.dayli.ly": sjc1,
}
