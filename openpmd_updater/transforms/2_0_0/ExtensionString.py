"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from openpmd_updater.transforms import ITransform
import numpy as np


class ExtensionString(ITransform):
    """
    Trasnforms an extension ID to a string attribute.

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/issues/151
    """
    
    def __init__(self, filename):
        """Open a file"""
        raise NotImplementedError("File opening not implemented!")
        # TODO: open backend
        # self.fb = backend(filename)

    def min_version(self):
        """Minimum openPMD standard version that is supported by this transformation"""
        return "1.0.0"

    def to_version(self):
        """openPMD standard version is fulfulled by this transformation"""
        return "2.0.0"

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        ext_list = {"ED-PIC": np.uint32(1)}

        fb.cd(None)
        extensionID = fb.get_attr("openPMDextension")
        fb.delete("openPMDextension")
        
        enabled_extensions = []
        enabledExtMask = 0
        for extension, bitmask in ext_list.items():
            # This uses a bitmask to identify activated extensions
            if (bitmask & extensionIDs) == bitmask:
                enabled_extensions.append(extension)
        
        fb.add_attr(
            "openPMDextension",
            np.string_(";".join(enabled_extensions))
        )
