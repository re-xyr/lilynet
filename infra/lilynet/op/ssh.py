from pyinfra.operations import files, systemd

sshd_config_result = files.put(
    src="lilynet/config/sshd/no-pwauth.conf",
    dest="/etc/ssh/sshd_config.d/no-pwauth.conf",
)
systemd.service(service="ssh", enabled=True, reloaded=sshd_config_result.changed)
