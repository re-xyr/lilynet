from pyinfra.operations import apk, files, openrc, server
from pyinfra.context import host
from pyinfra.facts.files import File
from lilynet.view import get_view

view = get_view(host)

# Install required packages

apk.packages(packages=["go", "xcaddy"])
if host.get_fact(File, "/usr/local/bin/caddy") is None:
    server.shell(
        name="Install Caddy",
        commands=[
            "xcaddy build --with github.com/caddy-dns/cloudflare --output /usr/local/bin/caddy"
        ],
    )

# Set up services

caddy_service_result = files.put(
    src="lilynet/config/init.d/caddy",
    dest="/etc/init.d/caddy",
    mode="0755",
)

# Set up Caddy

server.group(group="caddy")
server.user(user="caddy", group="caddy")
caddy_result = files.template(
    src="lilynet/config/caddy/Caddyfile.j2",
    dest="/etc/caddy/Caddyfile",
    # j2 variables
    local=view.local,
    global_secrets=view.global_secrets,
)
openrc.service(
    service="caddy",
    enabled=True,
    reloaded=caddy_service_result.changed or caddy_result.changed,
)

if caddy_result.changed:
    server.shell(
        name="Update Caddy CA",
        commands=["caddy trust"],
    )
