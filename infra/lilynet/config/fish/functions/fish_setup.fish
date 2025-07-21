function fish_setup
    curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher
    fisher install decors/fish-colored-man patrickf1/fzf.fish@v10.2 jorgebucaran/autopair.fish@1.0.4 gazorby/fish-exa joseluisq/gitnow@2.12.0 0rax/fish-bd@v1.3.3 jethrokuan/z ilancosman/tide@v6 nickeb96/puffer-fish
end
