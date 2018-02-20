"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from openpmd_updater.transforms.ITransform import ITransform
import numpy as np


class Version(ITransform):
    """
    Transforms the openPMD version.

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/projects/3
    """

    """Name and description of the transformation"""
    name = "version", "replace openPMD version identifier with new version"

    """Minimum openPMD standard version that is supported by this transformation"""
    min_version = "1.0.0"

    """openPMD standard version is fulfulled by this transformation"""
    to_version = "2.0.0"

    def __init__(self, backend):
        """Open a file"""
        self.fb = backend

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        self.fb.cd(None)
        self.fb.del_attr("openPMD")
        self.fb.add_attr("openPMD", np.string_(Version.to_version))
