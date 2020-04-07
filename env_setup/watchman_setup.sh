#!/bin/bash

PKGS=(
    "build-essential"
    "libssl-dev"
    "autoconf"
    "automake"
    "libtool"
    "python-dev"
    "python-setuptools"
    "python3-setuptools"
)

for I in ${PKGS[@]}
do
    sudo apt install ${I} -y
done


git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1
cd watchman
./autogen.sh
./configure --with-python=/usr/bin/python3 --enable-conffile=/etc/watchman.json
make
sudo make install