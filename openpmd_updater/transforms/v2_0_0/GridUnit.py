"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from ..ITransform import ITransform
import numpy as np


class GridUnit(ITransform):
    """
    GridSpacing: Per-Component UnitSI & UnitDimension

    In openPMD 1.*, mesh grid spacings were always spatial.
    openPMD 2.0 introduces a notation to allow arbitrary axes on meshes.

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/pull/122
        https://github.com/openPMD/openPMD-standard/pull/193
    """

    """Name and description of the transformation"""
    name = "gridUnit", "allow non-spatial gridSpacing in meshes"

    """Minimum openPMD standard version that is supported by this transformation"""
    min_version = "1.0.0"

    """openPMD standard version is fulfilled by this transformation"""
    to_version = "2.0.0"

    def __init__(self, backend):
        """Open a file"""
        self.fb = backend

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        try:
            self.fb.cd(None)
            basePath = "/data/"  # fixed in openPMD v1
            meshes_path = self.fb.get_attr("meshesPath").decode()
        except KeyError:
            print(
                "[Grid Unit transform] Input file has no 'meshesPath' attr, skipping transform! "
            )
            return

        iterations = self.fb.list_groups("/data/")

        for it in iterations:
            abs_meshes_path = "/data/" + str(it) + "/" + meshes_path
            #            vector/tensor                    and   scalar meshes
            all_meshes = self.fb.list_groups(abs_meshes_path) + self.fb.list_data(
                abs_meshes_path
            )

            self.fb.cd(abs_meshes_path)

            for mesh in all_meshes:
                old_grid_unit_SI = self.fb.get_attr("gridUnitSI", mesh)

                grid_ndim = len(self.fb.get_attr("gridSpacing", mesh))

                new_grid_unit_SI = (
                    np.ones((grid_ndim,), dtype=np.float64) * old_grid_unit_SI
                )

                self.fb.add_attr("gridUnitSI", new_grid_unit_SI, mesh)

                # openPMD 1.* dimensions were spatial (L)
                grid_unit_dimension = np.zeros((grid_ndim * 7,), dtype=np.float64)
                grid_unit_dimension[::7] = 1.0

                self.fb.add_attr("gridUnitDimension", grid_unit_dimension, mesh)
