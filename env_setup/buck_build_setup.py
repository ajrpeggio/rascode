#!/usr/bin/python3
import logging
import os
import subprocess
import sys


logger = logging.getLogger(__name__)


def repo_clone():
    buck_repo = "git clone https://github.com/facebook/buck.git"
    wm_repo = "https://github.com/facebook/watchman.git"
    

def watchman_setup():
    wm_url = "https://github.com/facebook/watchman.git"
    clone_cmd = f"git clone {wm_url} -b v4.9.0 --depth 1"
