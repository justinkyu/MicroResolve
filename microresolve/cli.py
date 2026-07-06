import sys

from .core import resolve

HELP = """
MicroResolve v0.1

Usage

python3 -m microresolve <hostname>

Example

python3 -m microresolve google.com
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    resolve(args[0])
