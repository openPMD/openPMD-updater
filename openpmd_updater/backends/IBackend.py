"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from abc import abstractmethod


class IBackend(object):
    """An I/O file format backend.
    Used to access and modify existing files with openPMD markup.
    """

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def can_handle(filename):
        """Check if a backend can handle a file."""
        raise NotImplementedError("File handling check not implemented!")

    @property
    @abstractmethod
    def version(self):
        """Return openPMD standard version of the file."""
        raise NotImplementedError("Version check not implemented!")

    @abstractmethod
    def cd(self, path):
        """Change current directory in file."""
        raise NotImplementedError("Directory change not implemented!")

    @abstractmethod
    def pwd(self, path):
        """Return current directory in file."""
        raise NotImplementedError("Directory pwd not implemented!")

    @abstractmethod
    def list_groups(self, path):
        """Return a list of groups in a path"""
        raise NotImplementedError("Group listing not implemented!")

    @abstractmethod
    def list_attrs(self, path):
        """Return a list of attributes on a path"""
        raise NotImplementedError("Attribute listing not implemented!")

    @abstractmethod
    def list_data(self, path):
        """Return a list of datasets in a path"""
        raise NotImplementedError("Data listing not implemented!")

    @abstractmethod
    def is_group(self, path):
        """Return if a path is a group"""
        raise NotImplementedError("Group check not implemented!")

    @abstractmethod
    def is_data(self, path):
        """Return if a path is a dataset"""
        raise NotImplementedError("Data check not implemented!")

    @abstractmethod
    def move(self, old_path, new_path):
        """Move (rename) a group, attribute or dataset"""
        raise NotImplementedError("Move (rename) not implemented!")

    @abstractmethod
    def del_group(self, path):
        """Remove a group, attribute or dataset"""
        raise NotImplementedError("Deleting group not implemented!")

    @abstractmethod
    def del_attr(self, name, path=None):
        """Remove a group, attribute or dataset"""
        raise NotImplementedError("Deleting atribute not implemented!")

    @abstractmethod
    def del_data(self, name):
        """Remove a group, attribute or dataset"""
        raise NotImplementedError("Deleting data not implemented!")

    @abstractmethod
    def add_group(self, path):
        """Add a new group at path"""
        raise NotImplementedError("Group adding not implemented!")

    @abstractmethod
    def add_attr(self, name, value, path=None):
        """Add a new attribute at path"""
        raise NotImplementedError("Attribute adding not implemented!")

    @abstractmethod
    def get_attr(self, name, path=None):
        """Read an attribute"""
        raise NotImplementedError("Attribute reading not implemented!")
