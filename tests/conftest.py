"""
This file is part of the openPMD-updater.

Copyright 2024 openPMD contributors
Authors: Sajid Ali
License: ISC
"""

import pytest
import requests


@pytest.fixture()
def get_file(tmp_path_factory):
    test_file = "structure.h5"
    test_file_url = (
        "https://github.com/openPMD/openPMD-example-datasets/raw/draft/structure.h5"
    )
    response = requests.get(test_file_url)

    test_file_path = tmp_path_factory.mktemp("data") / test_file

    with open(test_file_path, "wb") as out_file:
        out_file.write(response.content)

    print(test_file_path)

    return test_file_path
