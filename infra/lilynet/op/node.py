from pyinfra.operations import files, systemd, server, snap
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

# Install required packages

snap.package(packages=["node"], channel="22/stable", classic=True)

# Copy over and build server files

files.directory(path="/srv/frontend")
files.rsync(
    src="../frontend/",
    dest="/srv/frontend",
)

# Set up services

frontend_service_result = files.put(
    src="lilynet/config/systemd/lilynet-frontend.service",
    dest="/etc/systemd/system/lilynet-frontend.service",
)

if frontend_service_result.changed:
    systemd.daemon_reload()

# Turn up frontend

systemd.service(
    service="lilynet-frontend",
    restarted=True,
)
