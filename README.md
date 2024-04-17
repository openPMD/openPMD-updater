# openPMD Updater

[![CI:ubuntu](https://github.com/openPMD/openPMD-updater/actions/workflows/ci.yml/badge.svg)](https://github.com/openPMD/openPMD-updater/actions/workflows/ci.yml)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/openPMD-updater.svg)
[![License](https://img.shields.io/badge/license-ISC-blue.svg)](https://opensource.org/licenses/ISC)

This repository contains scripts to update existing files to *newer versions of the openPMD standard*.


## Rationale

We want our community to be able to move fast without pulling up a long legacy code trail for old versions.
We therefore motivate developers to always implement the latest stable version of the [openPMD standard](https://github.com/openPMD/openPMD-standard).

At the same time, we want that existing user data can always be read.
In order to achieve this, this repository provides a tool and modular library for lightweight meta-data updates.
Updates are only supported to go *forward* to newer releases.

**Developer perspective:** You only want to implement the latest version(s) of openPMD in order to reduce your development effort.
You update timely to new openPMD versions and deprecate or remove support for previous openPMD versions.
Now a user provides an openPMD file but the openPMD-standard version in it is too old compared to the standard implementation you rely on.
In a Python application, just import the module and (after a confirmation) auto-update the user-given file.
If you are not in a python environment, just reject the file gracefully with a note the version in the file is too old and point the user *here* to update their existing files.

**User perspective:** You are restoring "old" files from an archive and want to process it with a modern software that supports openPMD.
This software might only implement recent versions of openPMD, has no auto-update functionality and rejects your files.
Just run the updater command-line tool to update your files manually, then load it in aforementioned software.

## Install

[![pypi version](https://img.shields.io/pypi/v/openPMD-updater.svg)](https://pypi.python.org/pypi/openPMD-updater)
[![Spack Package](https://img.shields.io/badge/spack-py--openpmd--updater-blue.svg)](https://spack.io)
[![Conda Package](https://anaconda.org/ax3l/openpmd_updater/badges/version.svg)](https://anaconda.org/ax3l/updater)

Choose *one* of the install methods below to get started:

*TBD*

### From Source

```bash
git clone https://github.com/openPMD/openPMD-updater.git
cd openPMD-updater

# install dependencies
pip install -r requirements.txt

# optional: append --user
python setup.py install
```

## Usage

### CLI

We provide the command-line tools for individual files:

```bash
# optional: append --backup
openPMD_updater_h5 -i example.h5
```

### Module

Additionally, the updater tools can be used as *Python module* in your projects.
This allows you to offer a file update to users that try to use your tool with old versions of the openPMD standard (but you might only support newer versions).

```python
from openpmd_updater.Updater import Updater

updater = Updater("example.h5", verbose=False)
updater.update(target_version="2.0.0", in_place=True)

```

## Development

### Testing

```bash
export PYTHONPATH=$(pwd):$PYTHONPATH

# all
nosetests

# specific
nosetests tests/test_backend_h5.py

# manual
python tests/test_backend_h5.py
```

*note*: this changes your `example_files/1_1_0/structure.h5` files in-place.
`git checkout` it for a reset or do a comparison:

```bash
h5diff -c example_files/1_1_0/structure.h5.bak example_files/1_1_0/structure.h5
    attribute: <openPMD of </>> and <openPMD of </>>
    35 differences found
    Not comparable: <openPMDextension> is of class H5T_INTEGER and <openPMDextension> is of class H5T_STRING
    # ...
```
