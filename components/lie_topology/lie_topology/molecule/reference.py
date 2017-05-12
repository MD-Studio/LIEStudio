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

from lie_topology.common.serializable import Serializable
from lie_topology.common.contiguousMap import ContiguousMap
from lie_topology.common.exception import LieTopologyException

class AtomReference( Serializable ):
    
    def __init__( self, group_name=None, molecule_name=None, atom_name=None, external_index=None ):
        
        # Call the base class constructor with the parameters it needs
        Serializable.__init__( self, self.__module__, self.__class__.__name__ )
        
        self._group_name = group_name

        self._molecule_name = molecule_name

        self._atom_name = atom_name

        # index of the atm
        self._external_index = external_index
    
    def TryLink( self, root, referencing_molecule ):
        
        ## Try to find the linking atom
        ## While the molecule includes this reference
        ## in e.g. a bond, this reference could still point
        ## to a different molecule
        target_molecule = None
        target_group = None

        if self._group_name:
            # if we have a groupname find the root

            if root is None:
                raise LieTopologyException("AtomReference::UpcastFromMolecule", "a valid root object wasnt passed")
                
            target_group = root.groups[self._group_name]

        if self._molecule_name:

            if target_group is None:
                raise LieTopologyException("AtomReference::UpcastFromMolecule", "molecule does not contain a group reference")

            target_molecule = target_group.molecules[self._molecule_name]
        
        if self._atom_name is None or\
           target_molecule is None:
            return self

        return target_molecule.atoms[self._atom_name]