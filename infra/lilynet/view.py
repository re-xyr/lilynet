from pyinfra.api.host import Host
from lilynet.schema import Node
from lilynet.data.directory import nodes as directory
from lilynet.data.secrets import nodes as secrets, global_secrets


class View:
    def __init__(self, local: Node, local_secrets: dict[str, str], network: list[Node]):
        self.local = local
        self.local_secrets = local_secrets
        self.global_secrets = global_secrets
        self.network = network

    def __repr__(self):
        return f"<View {self.local.name}>"


def get_view(host: Host) -> View:
    local = directory.get(host.name)
    local_secrets = secrets.get(host.name)
    if local is None or local_secrets is None:
        raise ValueError(f"No entry found for host {host.name} in directory.")
    network = [node for node in directory.values() if node.name != local.name]
    return View(local, local_secrets, network)
