"""
This file is part of the openPMD-updater.

Copyright 2023 openPMD contributors
Authors: Axel Huebl, Sajid Ali
License: ISC
"""

from .Updater import Updater
import argparse


def parse_args():
    help_str: String = (
        "This is the openPMD updater HDF5 files.\n"
        + "It allows to update openPMD flavored files from openPMD standard {0} to {1}\n".format(
            111, 222
        )
    )
    parser = argparse.ArgumentParser(
        description=help_str, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("file", help="OpenPMD-series-filename", type=str)

    parser.add_argument("-b", "--backup", help="create a backup", action="store_true")
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_false"
    )
    parser.add_argument(
        "-t", "--target", help="target version to update to", type=str, default="2.0.0"
    )

    args = parser.parse_args()
    return args


def main():
    inputs = parse_args()
    updater = Updater(inputs.file, inputs.verbose)
    updater.update(inputs.target, not inputs.backup)
    # return code: non-zero is Unix-style for errors occurred
    # sys.exit(int(result_array[0]))


if __name__ == "__main__":
    main()
