# Lilynet infra orchestration

```sh
# Install dependencies
uv sync

# Run playbooks
uv run pyinfra inventory.py lilynet/op/[operation].py
```

## Operations

- `ip`: firewall rules and dummy interfaces
- `wg`: connect all WireGuard tunnels (internal, peers, router)
- `bgp`: BGP sessions, both on dn42 and clearnet
- `babel`: internal routing with the Babel protocol
- `dns`: authoritative DNS (daylily.network) and rDNS (2620:d7:6000::/48)
- `http`: HTTP(S) server via Caddy
