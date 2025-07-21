from pyinfra.operations import apk, files, openrc

apk.packages(packages=["nftables"])

nftables_result = files.put(
    src="lilynet/config/nftables.nft",
    dest="/etc/nftables.nft",
)

openrc.service(service="ufw", enabled=False, running=False)
openrc.service(
    service="nftables",
    enabled=True,
    restarted=nftables_result.changed,
)
