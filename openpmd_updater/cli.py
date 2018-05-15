"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""
import packaging.version
from openpmd_updater.Updater import Updater
import sys, getopt, os.path


def help():
    """ Print usage information for the command line interface"""
    print('This is the openPMD updater HDF5 files.\n')
    print('It allows to update openPMD flavored files from openPMD standard'
          ' {0} to {1}'.format(111,222))
    print('Usage:\n  openPMD_createExamples_h5 -i <fileName> [-v] [-b|--backup] [--target <2.0.0>]')
    sys.exit()


def parse_cmd(argv):
    """ Parse the command line arguments """
    file_name = ''
    verbose = False
    create_backup = False
    target_version = "2.0.0"
    try:
        opts, args = getopt.getopt(argv,"hvi:bt",
            ["file=", "backup"])
    except getopt.GetoptError:
        print('checkOpenPMD_h5.py -i <fileName>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-b", "--backup"):
            create_backup = True
        elif opt in ("-t", "--target"):
            target_version = arg
        elif opt in ("-i", "--file"):
            file_name = arg
    if not os.path.isfile(file_name):
        print("File '%s' not found!" % file_name)
        help()
    return file_name, verbose, target_version, not create_backup


def main():
    file_name, verbose, target_version, in_place = parse_cmd(sys.argv[1:])

    updater = Updater(file_name, verbose)
    updater.update(target_version, in_place)

    # return code: non-zero is Unix-style for errors occurred
    #sys.exit(int(result_array[0]))


if __name__ == "__main__":
    main()
