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

# optional: append --user
python setup.py install
```

## Usage

### CLI

We provide the command-line tools for individual files:

*TBD*

### Module

Additionally, the validator tools can be used as *Python module* in your projects.
This allows you to offer a file update to users that try to use your tool with old versions of the openPMD standard (but you might only support newer versions).

*TBD*

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
