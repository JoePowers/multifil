
#!/usr/bin/env python
# encoding: utf-8
"""
ti.py - A titin filament, with variable compliance

MORE ABOUT HOW TITIN WORKS

Created by Joe Powers and Dave Williams on 2017-02-17
"""


import numpy as np


class Titin:
    """This is all about the titin filament"""
    def __init__(self, parent_lattice, index, thick_face, thin_face):
        """Initialize the titin filament.

        Parameters:
            parent_lattice: calling half-sarcomere instance
            index: which titin filament this is (0-23)
            thick_face: List of thick filament faces' numerical orientation (0-5)
            thin_face: List of thin filament faces' numerical orientation (0-5)

        Returns:
            None"""
        # Name of the titin molecule
        self.index = index
        #
        self.parent_lattice = parent_lattice
        # Which thin filament are you closest to
        self.thin_face = thin_face
        # Link titin to that face of the thin filament
        self.thin_face.link_titin(self)
        # Which thick filament face are you attached to
        self.thick_face = thick_face
        # Link titin to the thick filament face
        self.thick_face.link_titin(self)

        #UNFINISHED

    def calc_tiangle(self):
        #Caclulate the angle that each titin makes relative to thick filament
        zln = self.parent_lattice.z_line
        last_node = self.thick_face.get_axial_location(-1)
        ls = self.parent_lattice.lattice_spacing
        angle = np.arctan(ls, zln-last_node)
        return angle

    def calc_tilength(self):
        #Calculate the length of each titin molecule
        zln = self.parent_lattice.z_line
        last_node = self.thick_face.get_axial_location(-1)
        ls = self.parent_lattice.lattice_spacing
        tilength = np.sqrt( (zln-last_node)**2 + ls**2 )
        return tilength

    def calc_axialtitinforce(self,kti):
        #kti is titin stiffness
        axialtitinforce = np.cos(0.5 * kti * tilength**2)
        return axialtitinforce

    def calc_radialtitinforce(self,kti):
        #kti is titin stiffness
        radialtitinforce = np.sin(0.5 * kti * tilength**2)
        return radialtitinforce
