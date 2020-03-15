#!/usr/bin/python3
import asyncio
import logging
import os
import subprocess


def logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
    )
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


log = logger.getLogger(__name__)


async def shell_run(self, cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    return {
        "stdout": [x.decode("UTF-8") for x in stdout.split(b"\n") if x != b""],
        "stderr": [x.decode("UTF-8") for x in stderr.split(b"\n") if x != b""],
    }


async def pip_install(pip_package):
    try:
        results = await self.shell_run(
            f"pip3 install {pip_package} -y"
        )
    if results["stdout"]:
        t_time = time.time() - self.start_time
        for result in results["stdout"]:
            log.info(result)
    except results["stderr"]:
        for result in results["stderr"]:
            log.error(result)



async def main():
    return


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    finally:
        loop.close()