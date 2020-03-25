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
    results = {
        "stdout": [x.decode("UTF-8") for x in stdout.split(b"\n") if x != b""],
        "stderr": [x.decode("UTF-8") for x in stderr.split(b"\n") if x != b""],
        "status": status_code,
        "success": True if status_code == 0 else False,
    }
    if results["stdout"]:
        for res in results["stdout"]:
            log.info(res)
    if results["stderr"]:
        for res in results["stderr"]:
            log.error(res)


def git_clone(repo_url, target_dir, branch, **kwargs):
    log.info("Starting Git Clone: %s. ", repo_url)
    try:
        git.Repo.clone_from(
            repo_url, target_dir, branch=branch, progress=CloneProgress(), **kwargs
        )
        log.info("Finished Git Clone: %s. ", repo_url)
    except Exception as e:
        raise e


def watchman_build():
    wm_path = "/tmp/watchman"
    os.chdir(wm_path)
    bash = "/bin/bash"
    make = "/usr/bin/make"
    cmds = [
        [bash, f"{wm_path}/autogen.sh"],
        [bash, f"{wm_path}/configure", "--with-python=/usr/bin/python3"],
        [make],
        [make, "install"],
    ]
    for cmd in cmds:
        shell_run(cmd)


def buck_build():
    buck_path = "/home/ajrpeggio/buck"
    os.chdir(buck_path)
    bash = "/bin/bash"
    ant = "/usr/bin/ant"
    cmds = [
        [ant],
        [bash, f"{buck_path}/bin/buck", "build", "--show-output", "buck"],
        ["/home/ajrpeggio/buck/buck-out/gen/ce9b6f2e/programs/buck.pex", "--help"],
    ]
    for cmd in cmds:
        shell_run(cmd)


def main():
    clone_kwargs = {"depth": 1}
    repo_list = [
        {
            "name": "buck",
            "url": "https://github.com/facebook/buck.git",
            "path": f"/home/ajrpeggio/buck/",
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
        git_clone(
            repo_url=i["url"], target_dir=i["path"], branch=i["branch"], **clone_kwargs
        )
    watchman_build()
    buck_build()
        


if __name__ == "__main__":
    sys.exit(main())