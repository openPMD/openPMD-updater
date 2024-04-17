"""
This file is part of the openPMD-updater.

Copyright 2023 openPMD contributors
Authors: Axel Huebl, Sajid Ali
License: ISC
"""

from .Updater import Updater
import pdb
import traceback
import sys
import argparse


def parse_args():
    help_str = (
        "This is the openPMD updater HDF5 files.\n"
        + "It allows to update openPMD flavored files from openPMD standard {0} to {1}\n".format(
            111, 222
        )
    )
    parser = argparse.ArgumentParser(
        description=help_str, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("file", help="openPMD-series-filename", type=str)

    parser.add_argument("-b", "--backup", help="create a backup", action="store_true")
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_false"
    )
    parser.add_argument(
        "-t", "--target", help="target version to update to", type=str, default="2.0.0"
    )
    parser.add_argument(
        "--pdb",
        help="wrap call in try/except with pdb post_mortem debugger",
        action="store_true",
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if not args.pdb:
        updater = Updater(args.file, args.verbose)
        updater.update(args.target, not args.backup)
        # return code: non-zero is Unix-style for errors occurred
        # sys.exit(int(result_array[0]))
    else:
        try:
            updater = Updater(args.file, args.verbose)
            updater.update(args.target, not args.backup)
        except:
            extype, value, tb = sys.exc_info()
            traceback.print_exc()
            pdb.post_mortem(tb)


if __name__ == "__main__":
    main()
