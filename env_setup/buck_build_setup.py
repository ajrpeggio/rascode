#!/usr/bin/python3
import git
import logging
import os
import subprocess
import sys

from typing import Dict, List



def logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


log = logger()


class CloneProgress(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
        if message:
            print(message)


def shell_run(cmd):
    proc = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    (stdout, stderr) = proc.communicate()
    status_code = proc.wait()
    return {
        "stdout": stdout,
        "stderr": stderr,
        "status": status_code,
        "success": True if status_code == 0 else False,
    }


def git_clone(repo_url, target_dir, branch, **kwargs):
    try:
        git.Repo.clone_from(
            repo_url, target_dir, branch=branch, progress=CloneProgress(), **kwargs
        )
    except Exception as e:
        raise e


def watchman_build():
    os.chdir("/tmp/watchman")
    bash = "/bin/bash"
    make = "/usr/bin/make"
    cmds = [
        [binbash, f"{watchman_path}/autogen.sh"],
        [binbash, f"{watchman_path}/configure", "--with-python=/usr/bin/python3"],
        [make],
        [make, "install"],
    ]
    for cmd in cmds:
        results = shell_run(cmd)
        if results["stdout"]:
            log.info(results["stdout"])
        if results["stderr"]:
            log.info(results["stderr"])


def main():
    clone_kwargs = {"depth": 1}
    repo_list = [
        {
            "name": "buck",
            "url": "https://github.com/facebook/buck.git",
            "path": f"/tmp/buck/",
            "branch": "master",
        },
        {
            "name": "watchman",
            "url": "https://github.com/facebook/watchman.git",
            "path": f"/tmp/watchman/",
            "branch": "v4.9.0",
        },
    ]
    """Cloning Watchman and Buck repos for Build. """
    for i in repo_list:
        name = i["name"]
        url = i["url"]
        folder = i["path"]
        branch = i["branch"]

        log.info("Starting clone for %s. ", name)
        git_clone(
            repo_url=url, target_dir=folder, branch=branch, **clone_kwargs
        )
        log.info("Finished cloning %s. ", i["name"])


if __name__ == "__main__":
    sys.exit(main())