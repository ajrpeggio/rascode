#!/usr/bin/python3
import apt
import sys

PKG_LIST = [
    "vim",
    "git",
    "default-jdk",
    "python2.7",
    "black",
    "ant",
    "libssl-dev",
    "autoconf",
    "automake",
    "libtool",
    "setuptools",
    "python-dev",
]


def install(cache, pkg_name):
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


def main(pkg_list):
    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    for i in pkg_list:
        install(cache, i)


if __name__ == "__main__":
    sys.exit(main(PKG_LIST))
