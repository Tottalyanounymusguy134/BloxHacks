#!/usr/bin/env python3
import argparse
import logging
import random
import socket
import sys
import time

parser = argparse.ArgumentParser(
    description="BloxHack, roblox hack tool for beginners"
)
parser.add_argument("host", nargs="?", help="Host to perform hack exercise on")
parser.add_argument(
    "-p", "--port", default=49152 - 65535, help="Port of roblox, usually 49152 - 65535", type=int
)
parser.add_argument(
    "-b",
    "--bypass",
    help="Bypass roblox defender firewall",
    type=int,
)
parser.add_argument(
    
)