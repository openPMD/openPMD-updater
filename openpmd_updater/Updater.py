"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

import packaging.version
from .backends.HDF5 import HDF5
from .transforms.v2_0_0 import (
    DataOrder,
    GridUnit,
    ParticleBoundary,
    ExtensionString,
    Version,
)


class Updater(object):
    """Updates a file from one openPMD standard to another.

    The updater class selects a suitable file format backend
    (see: openpmd_updater.backend.IBackend) for a given file and applies a set
    of transformations (see: openpmd_updater.transforms.ITransform) on it.
    """

    def __init__(self, filename, verbose=False):
        """Open a file with suiteable file format backend."""
        # supported file format backends
        self.backends = [HDF5]

        # dict of updates with each a list of transforms
        #   keys: "to_version" of targeted openPMD standard version
        #   values: ordered list of transforms
        self.updates = {
            "2.0.0": [
                DataOrder.DataOrder,  # must be before move of particleBoundary
                GridUnit.GridUnit,
                ParticleBoundary.ParticleBoundary,
                ExtensionString.ExtensionString,
                Version.Version,  # must be last
            ]
        }

        # select backend
        self.fb = None
        self.filename = filename
        self.verbose = verbose

        for b in self.backends:
            if self.verbose:
                print("[Updater] Trying file format {0}".format(b.__name__))
            if b.can_handle(filename):
                self.fb = b(filename)
                break
        if self.fb is None:
            raise RuntimeError(
                "No matching file format backend found for " "{0}!".format(filename)
            )

    def update(self, new_version="2.0.0", in_place=True):
        """Perform update to new version of the openPMD standard"""
        # detect openPMD standard version in file
        file_version = self.fb.version

        # check if new version is known by the updater
        update_valid = False
        if new_version not in self.updates.keys():
            raise RuntimeError(
                "Only updates to openPMD standard(s) '{0}' are " "supported!".format(
                    " ".join(self.updates.keys())
                )
            )

        if file_version == packaging.version.parse(new_version):
            print("[Updater] File is at already at the requested version!")
            return

        # select proper update depending on initial version
        #   note: multiple updates over intermediate openPMD standard releases are possible
        while file_version != packaging.version.parse(new_version):
            if file_version >= packaging.version.parse("1.0.0"):
                if file_version <= packaging.version.parse("1.1.0"):
                    update_valid = True
                    if self.verbose:
                        print(
                            "[Updater] Performing update from {0} to " "{1}".format(
                                file_version, new_version
                            )
                        )
                    for t in self.updates[new_version]:
                        self.fb.cd(None)
                        next_transform = t(self.fb)
                        if self.verbose:
                            name, desc = t.name
                            print("[Updater] Transform {0}: " "{1}".format(name, desc))
                        next_transform.transform(in_place)
                    file_version = packaging.version.parse(new_version)

            if not update_valid:
                raise RuntimeError(
                    "Unsupported openPMD standard '{0}' in file " "'{1}':".format(
                        file_version, self.filename
                    )
                )
