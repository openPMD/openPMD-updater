"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from openpmd_updater.transforms.ITransform import ITransform
import numpy as np


class ExtensionString(ITransform):
    """
    Transforms an extension ID to a string attribute.

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/issues/151
    """

    """Name and description of the transformation"""
    name = "extensionID", "replace the extensionID bitmask with a string list"

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

        ext_list = {"ED-PIC": np.uint32(1)}

        self.fb.cd(None)
        extensionIDs = self.fb.get_attr("openPMDextension")
        self.fb.del_attr("openPMDextension")

        enabled_extensions = []
        for extension, bitmask in ext_list.items():
            # This uses a bitmask to identify activated extensions
            if (bitmask & extensionIDs) == bitmask:
                enabled_extensions.append(extension)

        self.fb.add_attr(
            "openPMDextension",
            np.string_(";".join(enabled_extensions))
        )
