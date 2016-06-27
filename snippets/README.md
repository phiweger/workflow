## Snippets 

create folder and then save to it 

	mkdir .../Sublime\ Text\ 3/Packages/User/snippets/
    # here the snippets live

    # real snippets in repo
    # reformatted snippets for Sublime Text 3
    ~/config/sublime_text_3/snippets
    # symbolic link
    ln -s .../config/sublime_text_3/snippets .../Sublime\ Text\ 3/Packages/User/snippets

    # format the snippets in yaml format
    # shell (load virtual environment)
    workon lab3
    # in snippets directory
    python snip.py \
    -o snippets/misc.yaml \
    -f ~/config/sublime_text_3/snippets/
