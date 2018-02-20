"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""
from abc import abstractmethod


class ITransform(object):
    """Transform an openPMD file from one standard version to another.
    """
    
    @abstractmethod
    def __init__(self, backend):
        """Open a file"""
        raise NotImplementedError("File opening not implemented!")

    @property
    def name():
        """Name and description of the transformation"""
        raise NotImplementedError("Name and description not implemented!")

    @property
    def min_version():
        """Minimum openPMD standard version that is supported by this transformation"""
        raise NotImplementedError("Minimum supported openPMD standard version "
                                  "of this transformation not implemented!")

    @property
    def to_version():
        """openPMD standard version is fulfulled by this transformation"""
        raise NotImplementedError("Targeted openPMD standard version of "
                                  "this transformation not implemented!")

    @abstractmethod
    def transform(self, in_place=True):
        """Perform transformation"""
        raise NotImplementedError("Transformation not implemented!")
