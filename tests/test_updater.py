"""
This file is part of the openPMD-updater.

It checks that the updater works properly, by applying it to
an existing example file.

Note that this tests only makes sure that the updater does not crash -
not that it produces the correct update.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""
import unittest
from openpmd_updater.Updater import Updater

class Test_Updater(unittest.TestCase):
    """
    Class that tests the updater by applying it to an example file
    """

    def test_update(self):
        """
        Function that gets called by the tests
        """
        filename = "example_files/1_1_0/structure.h5"

        up = Updater(filename, verbose=True)

        up.update()

if __name__ == '__main__':
    unittest.main()
