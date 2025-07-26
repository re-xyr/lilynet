from dataclasses import KW_ONLY, dataclass, field


@dataclass
class Host:
    _: KW_ONLY
    hostname: str | None = None
    ipv4: str | None = None
    ipv6: str | None = None


@dataclass
class Wg:
    _: KW_ONLY
    peer_port: int
    peer_pubkey: str
    peer: Host
    local_port: int
    local_ll_ipv6: str


@dataclass
class WgTemplate:
    _: KW_ONLY
    local_port: int
    peer_pubkey: str
    peer_ll_ipv6: str


@dataclass
class Dn42Peer:
    _: KW_ONLY
    name: str
    asn: int
    underlay: Host
    wg: Wg
    multiprotocol: bool = True

    def __repr__(self):
        return f"<Peer {self.name} (AS{self.asn})>"


@dataclass
class Router:
    _: KW_ONLY
    host: Host
    ipv4s: list[str] = field(default_factory=list)
    ipv6s: list[str] = field(default_factory=list)
    ipv4_prefixes: list[str] = field(default_factory=list)
    ipv6_prefixes: list[str] = field(default_factory=list)


@dataclass
class Node:
    _: KW_ONLY
    name: str
    underlay: Host
    wg: WgTemplate
    clearnet: Router | None = None
    dn42: Router | None = None
    dn42_peers: list[Dn42Peer] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"<Node {self.name}>"


@dataclass
class NodeSecrets:
    _: KW_ONLY
    wg_privkey: str

    def __repr__(self) -> str:
        return "<NodeSecrets>"


@dataclass
class GlobalSecrets:
    _: KW_ONLY
    cloudflare_api_token: str
    vultr_bgp_password: str

    def __repr__(self) -> str:
        return "<GlobalSecrets>"
