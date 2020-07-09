#!/usr/bin/env python3
import asyncio
import logging
import os
import subprocess


PIP_PKGS = [
    "aiohttp",
    "black",
    "GitPython",
    "paramiko",
    "pyHS100",
    "PyMySQL",
    "requests",
    "xmltodict",
]


def logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def byte_decoder(msg: str()):
    if msg.decode("UTF-8"):
        return [x.decode("UTF-8") for x in msg.split(b"\n") if x != b""]
    else:
        raise TypeError("Positional Argument string is not UTF-8. ")


log = logger()


async def shell_run(cmd: str):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    return {
        "stdout": byte_decoder(stdout),
        "stderr": byte_decoder(stderr),
    }


async def pip_install(pip_package):
    results = await shell_run(f"/usr/bin/pip3 install {pip_package}")
    if results["stdout"]:
        for result in results["stdout"]:
            log.info(result)
    elif results["stderr"]:
        for result in results["stderr"]:
            log.error(result)


async def main(pip_pkg_list):
    futures = [pip_install(pkg) for pkg in pip_pkg_list]
    await asyncio.gather(*futures)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(PIP_PKGS))
    finally:
        loop.stop()
        loop.close()
