"""
This file is part of the openPMD-updater.

Copyright 2024 openPMD contributors
Authors: Axel Huebl, Sajid Ali
License: ISC
"""

import pytest
import os
import packaging.version
from openpmd_updater.backends.HDF5 import HDF5

@pytest.mark.order("first")
def test_can_handle(get_file):
    filepath = get_file
    print(filepath)
    assert os.path.exists(filepath) == True
    assert HDF5.can_handle(filepath)

@pytest.mark.order("second")
def test_read(get_file):
    fb = HDF5(get_file)

    assert fb.version == packaging.version.parse("1.1.0")
