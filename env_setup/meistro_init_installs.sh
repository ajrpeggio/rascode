#!/bin/bash

function aptInstalls() {
   arr=("$@")
   for i in ${arr[@]};
      do
          sudo apt install "${i}" -y
      done

}

INIT_PKGS=(
    "curl"
    "mercurial"
    "net-tools"
    "openssh-server"
    "git"
    "vim"
    "default-jdk"
    "python3-pip"
    "ruby"
)

aptInstalls ${INIT_PKGS[@]}

/usr/bin/python3 #{HOME}/env_setup/python_env.py
