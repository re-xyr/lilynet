if status is-interactive
    # Commands to run in interactive sessions can go here
    for abbr_name in (abbr)
        abbr -e $abbr_name
    end

    abbr -a vim nvim
    abbr -a vi nvim
    abbr -a ex nvim -e
    abbr -a view nvim -R
    abbr -a vimdiff nvim -d

    abbr -a top htop
    abbr -a ls eza
    abbr -a cat bat
    alias grep "grep --color=auto"

    abbr -a quit exit
end
