# openPMD Updater

[![Build Status `master`](https://img.shields.io/travis/openPMD/openPMD-validator/master.svg?label=master)](https://travis-ci.org/openPMD/openPMD-updater/branches)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/openPMD-updater.svg)
[![License](https://img.shields.io/badge/license-ISC-blue.svg)](https://opensource.org/licenses/ISC)

*TBD*


## Rationale

*TBD*


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

Additionally, the validator tools can be used as *Python module* in your projects.
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
