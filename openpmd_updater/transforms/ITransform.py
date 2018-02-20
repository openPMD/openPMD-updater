"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

class ITransform(object):
    """Transform an openPMD file from one standard version to another.
    """
    
    @abstractmethod
    def __init__(self, backend):
        """Open a file"""
        raise NotImplementedError("File opening not implemented!")

    @property
    @staticmethod
    @abstractmethod
    def name(self):
        """Name and description of the transformation"""
        raise NotImplementedError("Name and description not implemented!")

    @property
    @staticmethod
    @abstractmethod
    def min_version(self):
        """Minimum openPMD standard version that is supported by this transformation"""
        raise NotImplementedError("Minimum supported openPMD standard version "
                                  "of this transformation not implemented!")

    @property
    @staticmethod
    @abstractmethod
    def to_version(self):
        """openPMD standard version is fulfulled by this transformation"""
        raise NotImplementedError("Targeted openPMD standard version of "
                                  "this transformation not implemented!")

    @abstractmethod
    def transform(self, in_place=True):
        """Perform transformation"""
        raise NotImplementedError("Transformation not implemented!")
