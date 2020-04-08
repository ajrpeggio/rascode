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
)

aptInstalls ${INIT_PKGS[@]}