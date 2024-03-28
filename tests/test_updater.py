"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

import unittest
from openpmd_updater.Updater import Updater


class Test_Updater(unittest.TestCase):
    """
    ...
    """

    def test_update(self):
        """
        ...
        """
        filename = "example_files/1_1_0/structure.h5"

        up = Updater(filename, verbose=True)

        up.update()


if __name__ == "__main__":
    unittest.main()
