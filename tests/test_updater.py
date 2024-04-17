"""
This file is part of the openPMD-updater.

Copyright 2024 openPMD contributors
Authors: Axel Huebl, Sajid Ali
License: ISC
"""

from openpmd_updater.Updater import Updater


def test_update(get_file):
    up = Updater(get_file, verbose=True)
    up.update()
