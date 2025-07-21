from pyinfra.operations import apk, files, server

apk.packages(
    packages=["fish", "git", "bat", "eza", "neovim", "fastfetch", "htop", "fzf", "fd"]
)

server.user(user="root", shell="/usr/bin/fish")

files.sync(src="lilynet/config/fish/", dest="/root/.config/fish")
