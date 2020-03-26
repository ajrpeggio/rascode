#!/usr/bin/env python3
import apt
import sys

from typing import List


PKG_LIST = [
    "vim",
    "net-tools",
    "curl",
    "apache2",
    "git",
    "mercurial",
    "default-jdk",
    "openjdk-8-jre",
    "python2.7",
    "python3-pip",
    "openssh-server",
    "ant",
    "autoconf",
    "automake",
    "build-essential",
    "libssl-dev",
    "libtool",
    "python-dev",
    "python-setuptools",
    "python3-setuptools",
]


def install_pkgs(pkg_list: List):
    def apt_install(cache, pkg_name):
        pkg = cache[pkg_name]
        if pkg.is_installed:
            print(f"{pkg_name} is already installed. ")
            return
        else:
            pkg.mark_install()
        try:
            cache.commit()
        except Exception as e:
            print(sys.stderr, f"Unable to install package. {e}")
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    for pkg in pkg_list:
        apt_install(cache, pkg)


def main(pkg_list):
    install_pkgs(pkg_list)


if __name__ == "__main__":
    sys.exit(main(PKG_LIST))
