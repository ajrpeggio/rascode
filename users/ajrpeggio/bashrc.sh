# Default Editor
export EDITOR=vim

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User Specific Functions
bo ()
{
    cd $({ echo $PWD | cut -d '/' -f '1-6'; echo '/buck-out/gen/'; echo $PWD | cut -d '/' -f '7-'; } | tr -d '\n')
}

bi ()
{
    cd $(echo $PWD | cut -d '/' -f 1-6,9-)
}

# User Specific Aliases

alias rascode="cd ${HOME}/rascode/"

# _scm_prompt

export HISTSIZE=50000

RED_0=$(    tput setaf 1)
GREEN_0=$(  tput setaf 2)
RED="\[$RED_0\]"
GREEN="\[$GREEN_0\]"
CHECK="${GREEN}�"
CROSS="${RED}✘"

MY_PROMPT_0="\[\033[38;5;7m\]{\A}\[$(tput sgr0)\]\[\033[38;5;1m\][\[$(tput sgr0)\]\[\033[38;5;214m\]\u\[$(tput sgr0)\]\[\033[38;5;1m\]@\[$(tput sgr0)\]\[\033[38;5;39m\]\h\[$(tput sgr0)\]\[\033[38;5;1m\]:\[$(tput sgr0)\]\[\033[38;5;10m\]\w\[$(tput sgr0)\]\[\033[38;5;1m\]]\[$(tput sgr0)\]\[\033[38;5;99m\]"
MY_PROMPT_1="\[$(tput sgr0)\]\[\033[38;5;1m\] \\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"

_prompt_command() {
  LAST_STAT=$?
  case $LAST_STAT in
    0) PS1="${MY_PROMPT_0}${MY_PROMPT_1}" ;;
    *) PS1="${MY_PROMPT_0}${MY_PROMPT_1}" ;;
  esac
  history -a
  true
}

export PROMPT_COMMAND="_prompt_command"
