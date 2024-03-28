"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

import unittest
import packaging.version
from openpmd_updater.backends.HDF5 import HDF5


class Test_BackendHDF5(unittest.TestCase):
    """
    ...
    """

    def test_can_handle(self):
        """
        ...
        """
        self.assertEqual(HDF5.can_handle("example_files/1_1_0/structure.h5"), True)

    def test_read(self):
        """
        ...
        """
        filename = "example_files/1_1_0/structure.h5"

        fb = HDF5(filename)

        self.assertEqual(fb.version == packaging.version.parse("1.1.0"), True)


if __name__ == "__main__":
    unittest.main()
