#!/bin/bash


DEB_PKGS=(
    "python3"
    "vim"
    "build-essential"
    "libssl-dev"
    "autoconf"
    "automake"
    "libtool"
    "python-dev"
    "python-setuptools"
    "python3-setuptools"
)


BUCK_PKGS=(
    "watchman"
    "openjdk-8-jre"
    "ant"
    "python2.7"
    "git"
)


function aptInstalls() {
   arr=("$@")
   for i in ${arr[@]};
      do
          sudo apt install "${i}" -y
      done

} 


function buckInstall() {
    cd ${HOME}
    /usr/bin/git clone https://github.com/facebook/buck.git 
    cd buck
    ant
    ./bin/buck build --show-output buck
    buck-out/gen/ce9b6f2e/programs/buck.pex --help
    
    # Creating symlink for buck & buckd under /usr/bin
    sudo ln -s ${PWD}/bin/buck /usr/local/bin/buck
    sudo ln -s ${PWD}/bin/buckd /usr/local/bin/buckd
}


# Installing deps
aptInstalls ${DEB_PKGS[@]}
aptInstalls ${BUCK_PKGS[@]}

sudo apt update
sudo apt upgrade -y

# Calling Buck Install Function
buckInstall
