from pyinfra.operations import files, openrc, apk
from pyinfra.context import host
from lilynet.view import get_view

view = get_view(host)

# Install required packages

apk.packages(packages=["nodejs", "rsync"])

# Copy over and build server files

files.directory(path="/srv/frontend")
files.rsync(
    src="../frontend/",
    dest="/srv/frontend",
)

# Set up services

frontend_service_result = files.put(
    src="lilynet/config/init.d/lilynet-frontend",
    dest="/etc/init.d/lilynet-frontend",
    mode="0755",
)

# Turn up frontend

openrc.service(
    service="lilynet-frontend",
    enabled=True,
    restarted=True,
)
