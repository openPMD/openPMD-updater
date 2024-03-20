"""
This file is part of the openPMD-updater.

Copyright 2018 openPMD contributors
Authors: Axel Huebl, Remi Lehe
License: ISC
"""

from ..ITransform import ITransform
import numpy as np


class ParticleBoundary(ITransform):
    """
    Moves the `particleBoundary` attribute from the mesh records
    to the species records

    openPMD standard: 1.*.* -> 2.0.0

    Related openPMD-standard issues:
        https://github.com/openPMD/openPMD-standard/issues/105
    """

    """Name and description of the transformation"""
    name = (
        "particleBoundary",
        "move the particleBoundary attribute from the mesh records to the species records",
    )

    """Minimum openPMD standard version that is supported by this transformation"""
    min_version = "1.0.0"

    """openPMD standard version is fulfulled by this transformation"""
    to_version = "2.0.0"

    def __init__(self, backend):
        """Open a file"""
        self.fb = backend

    def transform(self, in_place=True):
        """Perform transformation"""
        if not in_place:
            raise NotImplementedError("Only in-place transformation implemented!")

        self.fb.cd(None)
        basePath = "/data/"  # fixed in openPMD v1
        meshes_path = self.fb.get_attr("meshesPath").decode()
        particles_path = self.fb.get_attr("particlesPath").decode()
        iterations = self.fb.list_groups("/data/")

        for it in iterations:
            # Get the old particle_boundary attribute, from the mesh level
            abs_meshes_path = "/data/" + str(it) + "/" + meshes_path
            particle_boundary = self.fb.get_attr("particleBoundary", abs_meshes_path)

            # Go through the list of species, and set this attribute
            # at the species level
            abs_particle_path = "/data/" + str(it) + "/" + particles_path
            all_species = self.fb.list_groups(abs_particle_path)
            self.fb.cd(abs_particle_path)
            for species in all_species:
                self.fb.add_attr("particleBoundary", particle_boundary, species)

            # Delete the old particle_boundary attribute
            self.fb.del_attr("particleBoundary", abs_meshes_path)
