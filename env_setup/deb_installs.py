#!/usr/bin/env python3
import apt
import sys

from typing import List


PKG_LIST = [
    "vim",
    "net-tools",
    "curl",
    "git",
    "mercurial",
    "default-jdk",
    "python3-pip",
    "openssh-server",
]



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



def install_pkgs(pkg_list: List):
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    for pkg in pkg_list:
        apt_install(cache, pkg)


def main(pkg_list):
    install_pkgs(pkg_list)


if __name__ == "__main__":
    sys.exit(main(PKG_LIST))
