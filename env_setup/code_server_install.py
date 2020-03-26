#!/usr/bin/env python3
import apt
import os
import requests
import subprocess
import sys
import tarfile

from typing import List


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


def get_file_req(url, save_location):
    r = requests.get(url, allow_redirects=True)
    with open(save_location, "wb") as f:
        f.write(r.content)


def unzip_file(zip_location):
    tf = tarfile.open(zip_location)
    tf.extractall("/tmp")



def bin_install(bin_map):
    get_file_req(bin_map["url"], bin_map["save_location"])
    unzip_file(bin_map["save_location"])
    if bin_map["name"] == "code-server":
        cs_name = bin_map["tarname"].replace(".tar.gz", "")
        os.rename(f"/tmp/{cs_name}/code-server", "/usr/bin/code-server")
    elif bin_map["name"] == "sshcode":
        os.rename("/tmp/sshcode", "/usr/bin/sshcode")
    else:
        raise Exception("Invalid Binary Package. ")


def main():
    cs_name = "code-server2.1698-vsc1.41.1-linux-x86_64.tar.gz"
    sc_name = "sshcode-linux-amd64.tar.gz"
    bin_list = [
        {
            "name": "sshcode",
            "tarname": sc_name,
            "url": f"https://github.com/cdr/sshcode/releases/download/v0.10.0/{sc_name}",
            "save_location": f"/tmp/{sc_name}",
        },
        {
            "name": "code-server",
            "tarname": cs_name,
            "url": f"https://github.com/cdr/code-server/releases/download/2.1698/{cs_name}",
            "save_location": f"/tmp/{cs_name}",
        },
    ]
    """apt install portion of main()"""
    pkg_list = [
        "golang",
    ]
    install_pkgs(pkg_list)

    """code-server install portion of main()"""
    for i in bin_list:
        bin_install(i)


if __name__ == "__main__":
    sys.exit(main())
