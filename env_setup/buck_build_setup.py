#!/usr/bin/python3
import git
import logging
import os
import sys

from typing import List


class CloneProgress(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
        if message:
            print(message)


def git_clone(repo_url, target_dir):
    try:
        git.Repo.clone_from(
            repo_url, target_dir, branch="master", progress=CloneProgress()
        )
    except Exception as e:
        raise e


def main():
    pwd = os.getcwd()
    # Cloning Buck and Watchman Repos
    repo_list = [
        {
            "name": "buck",
            "url": "https://github.com/facebook/buck.git",
            "path": f"{pwd}/buck/",
        },
        {
            "name": "watchman",
            "url": "https://github.com/facebook/buck.git",
            "path": f"{pwd}/watchman/",
        }
    ]
    for i in repo_list:
        git_clone(i["url"], i["path"])


if __name__ == "__main__":
    sys.exit(main())