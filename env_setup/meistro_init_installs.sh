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

ENV_PATH="${HOME}/env_setup"

PY_SCRIPTS=(
    "${ENV_PATH}/python_env.py"
    "${ENV_PATH}/dev_installs.py"
    "${ENV_PATH}/code_server_install.py"
)

for I in ${PY_SCRIPTS[@]}
do
    /usr/bin/python3 "${I}"
done
