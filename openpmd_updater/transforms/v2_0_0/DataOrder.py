"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl
License: ISC
"""

from ..ITransform import ITransform
import numpy as np


class DataOrder(ITransform):
    """
    Removes the `dataOrder` attribute from mesh records.

    The order of attributes arises naturally from flattened out memory layout.
    Regarding previously stored `dataOrder='F'` attributes, the update needs to
    invert such attributes.

    Affects the *base standard* attributes:
        - `axisLabels`
        - `gridSpacing`
        - `gridGlobalOffset`
        - `shape` of constant record components

    and the *ED-PIC* extension attributes:
        - `fieldBoundary`
        - `particleBoundary` (moved to particle records in openPMD 2.0)

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/issues/125
        https://github.com/openPMD/openPMD-standard/issues/129
        https://github.com/openPMD/openPMD-standard/issues/105
    """

    """Name and description of the transformation"""
    name = (
        "dataOrder",
        "remove the dataOrder attribute and transform Fortran attributes",
    )

    """Minimum openPMD standard version that is supported by this transformation"""
    min_version = "1.0.0"

    """openPMD standard version is fulfulled by this transformation"""
    to_version = "2.0.0"

    def __init__(self, backend):
        """Open a file"""
        self.fb = backend

        self.affected_attrs = [
            # base standard
            "axisLabels",
            "gridSpacing",
            "gridGlobalOffset",
            "shape",
            # ED-PIC
            "fieldBoundary",
            "particleBoundary",
        ]

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        self.fb.cd(None)
        basePath = "/data/"  # fixed in openPMD v1
        meshes_path = self.fb.get_attr("meshesPath").decode()

        iterations = self.fb.list_groups("/data/")

        for it in iterations:
            abs_meshes_path = "/data/" + str(it) + "/" + meshes_path
            #            vector/tensor                    and   scalar meshes
            all_meshes = self.fb.list_groups(abs_meshes_path) + self.fb.list_data(
                abs_meshes_path
            )

            self.fb.cd(abs_meshes_path)

            for mesh in all_meshes:
                old_data_order = self.fb.get_attr("dataOrder", mesh)
                if old_data_order == b"F":
                    # mesh record attributes
                    for attr_name in self.affected_attrs:
                        if attr_name in self.fb.list_attrs(mesh):
                            f_value = self.fb.get_attr(attr_name, mesh)
                            new_value = f_value[::-1]  # invert array
                            self.fb.add_attr(attr_name, new_value, mesh)

                    # constant vector/tensor mesh record components
                    if self.fb.is_group(mesh):
                        record_components = self.fb.list_groups(mesh)
                        for rc in record_components:
                            rc_path = mesh + "/" + rc
                            if "shape" in self.fb.list_attrs(rc_path):
                                f_value = self.fb.get_attr("shape", rc_path)
                                new_value = f_value[::-1]  # invert array
                                self.fb.add_attr("shape", new_value, rc_path)

                self.fb.del_attr("dataOrder", mesh)
