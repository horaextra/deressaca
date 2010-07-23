# These are shell utilities to improve the development process.

PROJECT_ROOT="$VIRTUAL_ENV/src"

alias manage="python $PROJECT_ROOT/manage.py"

function _fab_list () {
    # auto completion for fabfiles
    local cur="${COMP_WORDS[COMP_CWORD]}"
    FAB_OPTIONS=$(fab -l | grep '^ ' | awk '{ print $1 }')
    COMPREPLY=( $(compgen -W "$FAB_OPTIONS" -- ${cur}) )

    if [ "${COMPREPLY[*]}" = "$cur" ]
    then
        echo -e "\n$(fab -d $cur)"
        COMPREPLY=""
    fi
}
complete -o default -o nospace -F _fab_list fab
