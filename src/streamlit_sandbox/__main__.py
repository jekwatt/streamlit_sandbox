"""
By naming the top-level module __main__, it is possible to run this module as
a script by running:
`python -m streamlit_sandbox [args...]`
"""

import argparse
from sys import argv, path
from textwrap import dedent

from . import __version__


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="provide a one word message")
    args = parser.parse_args()
    print(args.message)


if __name__ == "__main__":
    main()
