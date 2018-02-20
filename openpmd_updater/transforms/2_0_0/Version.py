"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from openpmd_updater.transforms import ITransform
import numpy as np


class Version(ITransform):
    """
    Transforms the openPMD version.

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/projects/3
    """
    
    def __init__(self, backend):
        """Open a file"""
        self.fb = backend

    @property
    @staticmethod
    def name(self):
        """Name and description of the transformation"""
        return "version", "replace openPMD version identifier with new version"

    @property
    @staticmethod
    def min_version(self):
        """Minimum openPMD standard version that is supported by this transformation"""
        return "1.0.0"

    @property
    @staticmethod
    def to_version(self):
        """openPMD standard version is fulfulled by this transformation"""
        return "2.0.0"

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        fb.cd(None)
        fb.delete("openPMD")
        fb.add_attr("openPMD", np.string_(self.to_version))
