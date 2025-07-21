class Peer:
    def __init__(
        self,
        name: str,
        asn: int,
        endpoint: str,
        pubkey: str,
        local_port: int,
        local_link_ipv6: str,
        ipv6: str,
        ipv4: str | None,
        multiprotocol: bool = True,
    ):
        self.name = name
        self.asn = asn
        self.endpoint = endpoint
        self.pubkey = pubkey
        self.local_port = local_port
        self.local_link_ipv6 = local_link_ipv6
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.multiprotocol = multiprotocol

    def __repr__(self):
        return f"<Peer {self.name} (AS{self.asn})>"


class Downstream:
    def __init__(
        self,
        pubkey: str,
        ipv6: str,
        local_ipv4: str,
        public_ipv4: str | None = None,
        endpoint: str | None = None,
    ):
        self.pubkey = pubkey
        self.ipv6 = ipv6
        self.local_ipv4 = local_ipv4
        self.public_ipv4 = public_ipv4
        self.endpoint = endpoint

    def __repr__(self):
        return f"<Downstream {self.public_ipv4 if self.public_ipv4 is not None else self.local_ipv4}>"


class Node:
    def __init__(
        self,
        name: str,
        hostname: str,
        public_key: str,
        ipv4: str,
        ipv6: str,
        clearnet_ipv4: str,
        clearnet_ipv6: str,
        stable_port: int,
        stable_link_ipv6: str,
        peers: list[Peer] = [],
        downstreams: list[Downstream] = [],
    ):
        self.name = name
        self.hostname = hostname
        self.public_key = public_key
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.clearnet_ipv4 = clearnet_ipv4
        self.clearnet_ipv6 = clearnet_ipv6
        self.stable_port = stable_port
        self.stable_link_ipv6 = stable_link_ipv6
        self.peers = peers
        self.downstreams = downstreams

    def __repr__(self) -> str:
        return f"<Node {self.name}>"


class Secrets:
    def __init__(
        self,
        private_key: str,
    ):
        self.private_key = private_key

    def __repr__(self) -> str:
        return "<Secrets>"


class GlobalSecrets:
    def __init__(self, cloudflare_api_token: str, vultr_bgp_password: str):
        self.cloudflare_api_token = cloudflare_api_token
        self.vultr_bgp_password = vultr_bgp_password

    def __repr__(self) -> str:
        return "<GlobalSecrets>"
