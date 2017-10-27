# -*- coding: utf-8 -*-

from lie_md.gromacs_topology_amber import correctItp
from os.path import join
from twisted.logger import Logger

import os
import shutil

logger = Logger()


def set_gromacs_input(gromacs_config, workdir):
    """
    Create input files for gromacs.
    """
    # Write files and update links
    gromacs_config = copy_data_to_workdir(gromacs_config, workdir)

    # correct topology
    gromacs_config = fix_topology_ligand(gromacs_config, workdir)

    return fix_topology_protein(gromacs_config)


def fix_topology_protein(gromacs_config):
    """
    Adjust the topology of the protein
    """
    return gromacs_config


def fix_topology_ligand(gromacs_config, workdir):
    """
    Adjust topology for the ligand.
    """
    itp_file = join(workdir, 'ligand.itp')
    results = correctItp(
        gromacs_config['ligand_itp'], itp_file, posre=True)

    # Add charges and topology
    gromacs_config['charge'] = results['charge']
    gromacs_config['topology'] = itp_file

    return gromacs_config


def copy_data_to_workdir(config, workdir):
    """
    Move Gromacs related files to the Workdir
    """
    # Store protein file if available
    config['protein_pdb'] = store_structure_in_file(
        config['protein_pdb'], workdir, 'protein')

    # Store ligand file if available
    config['ligand_pdb'] = store_structure_in_file(
        config['ligand_pdb'], workdir, 'ligand')

    # Save ligand topology files
    config['ligand_itp'] = store_structure_in_file(
        config['ligand_itp'], workdir, 'input_GMX', ext='itp')

    return config


def store_structure_in_file(mol, workdir, name, ext='pdb'):
    """
    Store a molecule in a file if possible.
    """
    file_name = '{}.{}'.format(name, ext)
    dest = join(workdir, file_name)

    if mol is None:
        raise RuntimeError(
            "There is not {} available".format(name))

    elif os.path.isfile(mol):
        shutil.copy(mol, dest)

    elif os.path.isdir(mol):
        path = join(mol, file_name)
        store_structure_in_file(path, workdir, name, ext)

    else:
        with open(dest, 'w') as inp:
            inp.write(mol)

    return dest


def create_topology_with_pdb2gmx():
    pass

# PDB2GMX="$GMXBIN/pdb2gmx -v -f $dirn/$base.pdb -o $base.gro -p $base.top -ignh -ff $ForceField -water $SolModel"


# # 2. Position restraints
# #    * The position restraint fc (-posrefc) is bogus and 
# #      intended to allow easy replacement with sed.
# #      These will be placed under control of a #define
# PDB2GMX="$PDB2GMX -i $base-posre.itp -posrefc 999"


# # 3. Virtual sites
# $VirtualSites && PDB2GMX="$PDB2GMX -vsite hydrogens" 


# # 4. Add program options specified on command line (--pdb2gmx-option=value)
# PDB2GMX="$PDB2GMX $(program_options pdb2gmx
