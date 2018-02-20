"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""
import packaging.version
from openpmd_updater.backends import *
from openpmd_updater.transforms import *


class Updater(object):
    """Updates a file from one openPMD standard to another.

    The updater class selects a suitable file format backend
    (see: openpmd_updater.backend.IBackend) for a given file and applies a set
    of transformations (see: openpmd_updater.transforms.ITransform) on it.
    """
    # supported file format backends
    backends = [HDF5]

    # dict of updates with each a list of transforms
    #   keys: "to_version" of targeted openPMD standard version
    #   values: ordered list of transforms
    updates = {
        "2.0.0" : [
            2_0_0.ExtensionString,
            2_0_0.Version
        ]
    }

    def __init__(self, filename, verbose=False):
        """Open a file with suiteable file format backend.
        """
        # select backend
        self.fb = None
        self.filename = filename
        self.verbose = verbose

        for b in backends:
            if self.verbose:
                print("[Updater] Trying file format {0}".format(type(b)))
            if b.can_handle(filename):
                self.fb = b(filename)
                break
        if self.fb is None:
            raise RuntimeError("No matching file format backend found for "
                               "{0}!".format(filename))

    def update(self, new_version="2.0.0", in_place=True):
        """Perform update to new version of the openPMD standard"""
        # detect openPMD standard version in file
        file_version = self.fb.version()

        update_valid = False
        if packaging.version(new_version) != packaging.version("2.0.0"):
            raise RuntimeError("Only updates to openPMD standard '{0}' "
                               "are supported!".format(new_version)
        
        if file_version >= packaging.version("1.0.0"):
            if file_version <= packaging.version("1.1.0"):
                update_valid = True
                if self.verbose:
                    print("[Updater] Performing update from {0} to "
                          "{1}".format(file_version, new_version)
                for t in updates["2.0.0"]:
                    self.fb.cd(None)
                    next_transform = t(self.fb)
                    if self.verbose:
                        print("[Updater] Transform: {0}".format(next_transform.name)
                    next_transform.transform(in_place)

        if not update_valid:
            raise RuntimeError("Unsupported openPMD standard '{0}' in file "
                               "'{1}':".format(file_version, self.filename))
