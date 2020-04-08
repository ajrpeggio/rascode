#!/bin/bash

function aptInstalls() {
   arr=("$@")
   for i in ${arr[@]};
      do
          sudo apt install "${i}" -y
      done

}

WM_PKGS=(
    "build-essential"
    "libssl-dev"
    "autoconf"
    "automake"
    "libtool"
    "python-dev"
    "python-setuptools"
    "python3-setuptools"
)

aptInstalls ${WM_PKGS[@]}


git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1
cd watchman
./autogen.sh
./configure --with-python=/usr/bin/python3 --enable-conffile=/etc/watchman.json
make
sudo make install

###
###

BUCK_PKGS=(
    "openjdk-8-jre"
    "ant"
    "python2.7"
    "git"
)

aptInstalls ${BUCK_PKGS[@]}


git clone https://github.com/facebook/buck.git
cd buck
ant
./bin/buck build --show-output buck
buck-out/gen/ce9b6f2e/programs/buck.pex --help

sudo ln -s ${PWD}/bin/buck /usr/bin/buck
sudo ln -s ${PWD}/bin/buckd /usr/bin/buckd


