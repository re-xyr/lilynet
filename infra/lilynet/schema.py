from dataclasses import KW_ONLY, dataclass, field


@dataclass
class Host:
    _: KW_ONLY
    hostname: str | None = None
    ipv4: str | None = None
    ipv6: str | None = None

    def get_ip(self) -> str:
        if self.ipv6:
            return self.ipv6
        elif self.ipv4:
            return self.ipv4
        else:
            raise ValueError("Host must have either ipv4 or ipv6 set")

    def get_hostname(self) -> str:
        if self.hostname:
            return self.hostname
        else:
            return self.get_ip()


@dataclass
class Interface(Host):
    _: KW_ONLY
    ipv4_mask: int | None = None  # If none, we make this a point-to-point link
    ipv6_mask: int | None = 64


@dataclass
class Tunnel:
    _: KW_ONLY
    peer: Host


@dataclass
class Direct(Tunnel):
    _: KW_ONLY


@dataclass
class Wg(Tunnel):
    _: KW_ONLY
    peer_port: int
    peer_pubkey: str
    local_port: int | None = None  # If none, then we use PersistentKeepalive
    local: Interface
    local_privkey: str | None = None  # Set to none to use the node-default key


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
class Upstream:
    _: KW_ONLY
    name: str
    asn: int
    ipv4: bool = True
    ipv6: bool = True
    multihop: bool = False
    underlay: Host
    tunnel: Tunnel
    password: str | None = None


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
    upstreams: list[Upstream] = field(default_factory=list)
    dn42: Router | None = None
    dn42_peers: list[Dn42Peer] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"<Node {self.name}>"
