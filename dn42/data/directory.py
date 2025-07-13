from dn42.data.schema import Node
from dn42.data.nodes.ewr1 import ewr1
from dn42.data.nodes.sjc1 import sjc1

nodes: dict[str, Node] = {
    "ewr1.dn42.dayli.ly": ewr1,
    "sjc1.dn42.dayli.ly": sjc1,
}
