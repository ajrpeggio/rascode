#!/usr/bin/python3
import argparse
import logging

from pyHS100 import SmartPlug


log = logging.getLogger(__name__)


def on(plug: SmartPlug):
    if plug.is_on:
        print("The Plug is already on. ")
    else:
        plug.turn_on()


def off(plug: SmartPlug):
    if plug.is_off:
        print("The Plug is already off. ")
    else:
        plug.turn_off()


def main(args):
    plug = SmartPlug(args.plug_ip)
    if args.on:
        on(plug)
    elif args.off:
        off(plug)
    else:
        raise Exception("Invalid plug command. ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="spcli.py",
        description="Quick CLI for Smart Plug",
        usage="//%(prog)s [options]",
    )
    parser.add_argument(
        "plug_ip", type=str
    )
    parser.add_argument(
        "-o", "--on", action="store_true", help="Turns on Plug"
    )
    parser.add_argument(
        "-f", "--off", action="store_true", help="Turns off Plug"
    )
    args = parser.parse_args()
    main(args)
