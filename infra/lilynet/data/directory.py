from lilynet.schema import Node
from lilynet.data.nodes.nyc1 import nyc1
from lilynet.data.nodes.tyo1 import tyo1
from lilynet.data.nodes.sjc1 import sjc1

nodes: dict[str, Node] = {
    "nyc1.node.dayli.ly": nyc1,
    "tyo1.node.dayli.ly": tyo1,
    "sjc1.node.dayli.ly": sjc1,
}
