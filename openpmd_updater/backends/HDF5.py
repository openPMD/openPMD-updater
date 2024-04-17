"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from .IBackend import IBackend
import packaging.version
import h5py as h5


class HDF5(IBackend):
    """HDF5 File handling."""

    def __init__(self, filename):
        """Open a HDF5 file"""

        if self.can_handle(filename):
            self.fh = h5.File(filename, "r+")
            self.pwd = self.fh["/"]
        else:
            raise RuntimeError("HDF5 backend can not open non-HDF5 files!")

    @staticmethod
    def can_handle(filename):
        """Check if filename is a HDF5 file."""
        signature = b"\x89HDF\r\n\x1a\n"
        try:
            with open(filename, "rb") as f:
                header = f.read(8)
                return header == signature
        except:
            return False

    @property
    def version(self):
        """Return openPMD standard version of the file."""
        ver_string = self.fh.attrs["openPMD"].decode()
        return packaging.version.parse(ver_string)

    def cd(self, path):
        """Change current directory in file."""
        if path is None:
            self.pwd = self.fh["/"]
        else:
            self.pwd = self.pwd[path]

    def pwd(self, path):
        """Return current directory in file."""
        self.pwd.name

    def list_groups(self, path):
        """Return a list of groups in a path"""
        cur_path = self.pwd[path]
        return list(filter(lambda x: type(cur_path[x]) is h5.Group, cur_path.keys()))

    def list_attrs(self, path):
        """Return a list of attributes on a path"""
        cur_path = self.pwd[path]
        return list(cur_path.attrs.keys())

    def list_data(self, path):
        """Return a list of datasets in a path"""
        cur_path = self.pwd[path]
        return list(filter(lambda x: type(cur_path[x]) is h5.Dataset, cur_path.keys()))

    def is_group(self, path):
        """Return if a path is a group"""
        cur_path = self.pwd[path]
        return type(cur_path) is h5.Group

    def is_data(self, path):
        """Return if a path is a dataset"""
        cur_path = self.pwd[path]
        return type(cur_path) is h5.Dataset

    def move(self, old_path, new_path):
        """Move (rename) a group, attribute or dataset"""
        if new_path == old_path:
            raise RuntimeError("old_path and new_path are identical!")

        obj = self.pwd["old_path"]
        if type(obj) is h5.Group:
            self.pwd.move(old_path, new_path)
        elif type(obj) is h5.Dataset:
            self.pwd.move(old_path, new_path)
        elif type(obj) is h5.Attribute:
            self.pwd.attrs[new_path] = self.pwd.attrs[old_path]
            self.delete(old_path)
        else:
            NotImplementedError(
                "Move is not implemented for " "'{0}' at '{1}'!".format(
                    type(obj), old_path
                )
            )

    def del_goup(self, name):
        """Remove a group, attribute or dataset"""
        del self.pwd[name]

    def del_attr(self, name, path=None):
        """Remove a group, attribute or dataset"""
        if path is None:
            del self.pwd.attrs[name]
        else:
            del self.pwd[path].attrs[name]

    def del_data(self, name):
        """Remove a group, attribute or dataset"""
        del self.pwd[name]

    def add_group(self, path):
        """Add a new group at path"""
        self.pwd.create_group[path]

    def add_attr(self, name, value, path=None):
        """Add a new attribute at path"""
        if path is None:
            self.pwd.attrs[name] = value
        else:
            self.pwd[path].attrs[name] = value

    def get_attr(self, name, path=None):
        """Read an attribute"""
        if path is None:
            return self.pwd.attrs[name]
        else:
            return self.pwd[path].attrs[name]
