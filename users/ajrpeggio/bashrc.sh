#!/bin/bash
# Default Editor
export EDITOR=vim
export HISTSIZE=50000

# Source global definitions
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# User Specific Aliases
alias rascode="cd ${HOME}/rascode/"
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'

# User Specific Functions
bo ()
{
    cd $({ echo $PWD | cut -d '/' -f '1-6'; echo '/buck-out/gen/'; echo $PWD | cut -d '/' -f '7-'; } | tr -d '\n')
}

bi ()
{
    cd $(echo $PWD | cut -d '/' -f 1-6,9-)
}

# _scm_prompt
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

case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
