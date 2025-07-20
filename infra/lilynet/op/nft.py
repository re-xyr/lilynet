from pyinfra.operations import apt, files, systemd

apt.packages(packages=["nftables"])

nftables_result = files.put(
    src="lilynet/config/nftables.conf",
    dest="/etc/nftables.conf",
)
systemd.service(service="nftables", enabled=True, restarted=nftables_result.changed)
