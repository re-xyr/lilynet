# Lilynet infra orchestration

Lilynet ([AS401736](https://bgp.tools/as/401736), [AS4242421919](https://explorer.dn42.dev/#/AS4242421919)) is [daylily](https://dayli.ly)'s personal experimental network. This network is programmatically orchestrated via [pyinfra](https://pyinfra.com), a code-first alternative to Ansible.

## Usage

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

## dn42 Peering

I am open to peering on [dn42](https://wiki.dn42.us). See https://dayli.ly/dn42 for details.

## License

This source code is provided under [GNU General Public License v3.0 or later (`GPL-3.0-or-later`)](LICENSE).
