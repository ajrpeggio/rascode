#!/bin/bash

BIND_PKGS=(
    "bind9"
    "bind9utils"
    "bind9-doc"
    "resolvconf"
)

function aptInstalls() {
   arr=("$@")
   for i in ${arr[@]};
      do
          sudo apt install "${i}" -y
      done

}

aptInstalls ${BIND_PKGS[@]}
