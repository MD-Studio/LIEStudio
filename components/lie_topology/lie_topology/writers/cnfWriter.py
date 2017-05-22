#
# @cond ___LICENSE___
#
# Copyright (c) 2017 K.M. Visscher and individual contributors.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# @endcond
#

import sys
import os
import numpy as np

from lie_topology.common.exception   import LieTopologyException

def _PrintHeader( ofstream ):
    
    ofstream.write( "TITLE\n"+\
                    "\tLie_topology converted file\n"+\
                    "END\n" )

def _WriteStep( ofstream, step ) :

    ofstream.write( "TIMESTEP\n"+\
                    "%i %f\n" % ( step.model_number, step.time )+\
                    "END\n" )

def _MoleculeFormat( molecule, array, n_residue, n_atom ):

    mol_type_string = ""

    molecule_number = molecule.identifier
    molecule_name   = molecule.type_name
    
    for atom_key, atom in molecule.atoms.items():

        atom_number = atom.identifier
        atom_name   = atom.type_name
        xyz         = array[n_atom]
            
        mol_type_string += "%5i %-5s %-5s%7s%15.9f%15.9f%15.9f \n" %\
        ( molecule_number, molecule_name, atom_name, atom_number, xyz[0], xyz[1], xyz[2] )
        
        n_atom+=1

    return mol_type_string

def _SolventFormat( solvent, array, n_residue, n_atom ):

    top_type_string = ""

    remainder = len(array) - n_residue
    solvent_atom_count = solvent.atom_count
    n_solv = remainder / solvent_atom_count

    if (remainder % solvent_atom_count) != 0:
        raise LieTopologyException( "CnfGenerator::_PrintPositions", "Mismatch between remaining array size and number of solvent atoms")
    
    for i in range(0, n_solv):

        top_type_string += _MoleculeFormat( solvent, array, n_residue, n_atom )

        n_residue+=1
        n_atom+=solvent.atom_count

def _TopologicalFormat( topology, array ):

    top_type_string = ""

    num_positions = len( array )
    num_solute_atoms = topology.solute_atom_count

    if num_positions < num_solute_atoms:
        raise LieTopologyException( "CnfGenerator::_PrintPositions", "Writing of solute positions requires at least %i coordinates, currently %i present" % (num_solute_atoms, num_positions) )

    n_residue=0
    n_atom=0
    for group in topology.groups.values():
        for molecule_key, molecule in group.molecules.items():

            top_type_string += _MoleculeFormat( molecule, array, n_residue, n_atom )

            n_residue+=1
            n_atom+=molecule.atom_count
            
    return top_type_string, n_residue, n_atom

def _PrintPositions( ofstream, structure ):
    
    position_string, n_residue, n_atom = _TopologicalFormat( structure.topology, structure.coordinates )
    solvent_string = ""

    if structure.topology.solvent is not None:
        solvent_string = _MoleculeFormat( structure.topology.solvent, array, n_residue, n_atom )

    ofstream.write( "POSITION\n"+\
                    position_string+\
                    solvent_string+\
                    "END\n" )

def _PrintVelocities( ofstream, structure ):
    
    velocity_string, n_residue, n_atom = _TopologicalFormat( structure.topology, structure.velocities )
    solvent_string = ""

    if structure.topology.solvent is not None:
        solvent_string = _MoleculeFormat( structure.topology.solvent, array, n_residue, n_atom )

    ofstream.write( "VELOCITY\n"+\
                    velocity_string+\
                    solvent_string+\
                    "END\n" )

def _PrintForces( ofstream, structure ):
    
    forces_string, n_residue, n_atom = _TopologicalFormat( structure.topology, structure.forces )
    solvent_string = ""

    if structure.topology.solvent is not None:
        solvent_string = _MoleculeFormat( structure.topology.solvent, array, n_residue, n_atom )

    ofstream.write( "FREEFORCE\n"+\
                    "# Note lie_topology does not recognice differences between free and cons force"+\
                    forces_string+\
                    solvent_string+\
                    "END\n" )

def _PrintLattice( ofstream, lattice ):

    box_type = None
    
    if lattice.edge_lenghts is None or\
       lattice.edge_angles  is None or\
       lattice.rotation     is None or\
       lattice.offset       is None:

        raise LieTopologyException( "CnfGenerator::_PrintLattice", "Full lattice definition is required")


    ofstream.write( "GENBOX\n"+\
                    "%-15.9f%-15.9f%-15.9f\n" % ( lattice.edge_lenghts[0], lattice.edge_lenghts[1], lattice.edge_lenghts[2] )+\
                    "%-15.9f%-15.9f%-15.9f\n" % ( lattice.edge_angles[0],  lattice.edge_angles[1],  lattice.edge_angles[2] )+\
                    "%-15.9f%-15.9f%-15.9f\n" % ( lattice.rotation[0],     lattice.rotation[1],     lattice.rotation[2] )+\
                    "%-15.9f%-15.9f%-15.9f\n" % ( lattice.offset[0],       lattice.offset[1],       lattice.offset[2] )+\
                    "END\n" )

def WriteCnf( ofstream, structures ):

    _PrintHeader( ofstream )

    for structure in structures:

        if structure.topology is None:
            raise LieTopologyException( "CnfGenerator::_PrintPositions", "A structure topology is required to write cnf files")

        if structure.step is not None:
            _WriteStep( ofstream, structure.step )
        
        if structure.coordinates is not None:
            _PrintPositions( ofstream, structure )

        if structure.velocities is not None:
            _PrintVelocities( ofstream, structure )
        
        if structure.forces is not None:
            _PrintForces( ofstream, structure )
        
        if structure.lattice is not None:
            _PrintLattice( ofstream, structure.lattice )

    #fileHandle.write( self.result )
