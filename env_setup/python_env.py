#!/usr/bin/python3
import asyncio
import logging
import os
import subprocess


<<<<<<< HEAD
PIP_PKGS = ["aiohttp", "paramiko", "PyMySQL", "xmltodict"]


def logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
=======
def logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
    )
>>>>>>> 58eacd420cf06182f83d0114f4cace7df33c5d58
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


<<<<<<< HEAD
log = logger()


async def shell_run(cmd):
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
    except Exception as e:
        raise e
=======
log = logger.getLogger(__name__)


async def shell_run(self, cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
>>>>>>> 58eacd420cf06182f83d0114f4cace7df33c5d58
    return {
        "stdout": [x.decode("UTF-8") for x in stdout.split(b"\n") if x != b""],
        "stderr": [x.decode("UTF-8") for x in stderr.split(b"\n") if x != b""],
    }


async def pip_install(pip_package):
<<<<<<< HEAD
    results = await shell_run(f"/usr/bin/pip3 install {pip_package}")
    if results["stdout"]:
        for result in results["stdout"]:
            log.info(result)
    elif results["stderr"]:
=======
    try:
        results = await self.shell_run(
            f"pip3 install {pip_package} -y"
        )
    if results["stdout"]:
        t_time = time.time() - self.start_time
        for result in results["stdout"]:
            log.info(result)
    except results["stderr"]:
>>>>>>> 58eacd420cf06182f83d0114f4cace7df33c5d58
        for result in results["stderr"]:
            log.error(result)


<<<<<<< HEAD
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
=======

async def main():
    return


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    finally:
        loop.close()
>>>>>>> 58eacd420cf06182f83d0114f4cace7df33c5d58
