from pyinfra.operations import apt, files, systemd, server
from pyinfra.context import host
from pyinfra.facts.files import File
from lilynet.view import get_view

view = get_view(host)

# Install required packages

repo_updated = apt.repo(
    src="deb https://dl.cloudsmith.io/public/caddy/xcaddy/deb/debian any-version main"
)
if repo_updated.changed:
    apt.update()
apt.packages(packages=["golang-go", "xcaddy"])

# Install Caddy

if host.get_fact(File, "/usr/local/bin/caddy") is None:
    server.shell(
        name="Install Caddy",
        commands=[
            "xcaddy build --with github.com/caddy-dns/cloudflare --output /usr/local/bin/caddy"
        ],
    )

# Set up services

caddy_service_result = files.put(
    src="lilynet/config/systemd/caddy.service",
    dest="/etc/systemd/system/caddy.service",
)

if caddy_service_result.changed:
    systemd.daemon_reload()

# Set up Caddy

caddy_result = files.template(
    src="lilynet/config/caddy/Caddyfile.j2",
    dest="/etc/caddy/Caddyfile",
    # j2 variables
    local=view.local,
    global_secrets=view.global_secrets,
)
if caddy_result.changed:
    server.shell(
        name="Update Caddy CA",
        commands=["caddy trust"],
    )
systemd.service(
    service="caddy",
    enabled=True,
    reloaded=caddy_service_result.changed or caddy_result.changed,
)
