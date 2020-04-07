#!/bin/bash

PKGS=(
    "openjdk-8-jre"
    "ant"
    "python2.7"
    "git"
)

for I in ${PKG[@]}
do
    sudo apt install ${I} -y
done


git clone https://github.com/facebook/buck.git
cd buck
ant
./bin/buck build --show-output buck
buck-out/gen/ce9b6f2e/programs/buck.pex --help

sudo ln -s ${PWD}/bin/buck /usr/bin/buck
sudo ln -s ${PWD}/bin/buckd /usr/bin/buckd