
import json
import yaml

from lie_topology.molecule.molecule import Molecule
from lie_topology.molecule.blueprint import Blueprint
from lie_topology.molecule.structure import Structure
from lie_topology.parsers.mtbParser import ParseMtb
from lie_topology.parsers.cnfParser import ParseCnf
from lie_topology.parsers.ifpParser import ParseIfp
from lie_topology.parsers.pdbParser import ParsePdb
from lie_topology.parsers.groParser import ParseGro
from lie_topology.parsers.sdfParser import ParseSdf
from lie_topology.parsers.mol2Parser import ParseMol2

from lie_topology.utilities.makeTopology import MakeSequence

from lie_topology.writers.cnfWriter import WriteCnf
from lie_topology.writers.gromosTopologyWriter import WriteGromosTopology

from lie_topology.molecule.crystal import BoxVectorsToLattice, LatticeToBoxVectors


def main():

    # with open( "../tests/data/pdb/peptide.pdb", 'r') as ifstream:    
        
    #     pdb_structures = ParsePdb( ifstream )
        
    #     with open( "../tests/data/cnf/test_write.cnf", 'w') as ofstream:
            
    #         WriteCnf( ofstream, pdb_structures )
    
    # with open( "../tests/data/cnf/md_fX_apixaban_1.cnf", 'r') as ifstream:

    #     cnf_structures = ParseCnf( ifstream )

    #     with open( "../tests/data/cnf/test_write2.cnf", 'w') as ofstream:
            
    #         WriteCnf( ofstream, cnf_structures )
    
    # with open( "../tests/data/gro/run1_combined_pbc.gro", 'r') as ifstream:

    #     gro_structures = ParseGro( ifstream )

    #     with open( "../tests/data/cnf/test_write3.cnf", 'w') as ofstream:
            
    #         WriteCnf( ofstream, gro_structures )

    # with open( "../tests/data/sdf/BHC2.sdf", 'r') as ifstream:

    #     sdf_structures = ParseSdf( ifstream )

    #     with open( "../tests/data/cnf/test_write4.cnf", 'w') as ofstream:
            
    #         WriteCnf( ofstream, sdf_structures )     

    # with open( "../tests/data/mol2/BHC2.mol2", 'r') as ifstream:

    #     mol2_structures = ParseMol2( ifstream )

    #     with open( "../tests/data/cnf/test_write5.cnf", 'w') as ofstream:
            
    #         WriteCnf( ofstream, mol2_structures )  


    with open( "../tests/data/mtb/54a7.mtb", 'r') as mtb_ifstream,\
         open( "../tests/data/ifp/54a7.ifp", 'r') as ifp_ifstream:

        blueprint = ParseMtb( mtb_ifstream )
        forcefield = ParseIfp( ifp_ifstream )

        topology = MakeSequence( forcefield, blueprint, ["NH3+","ALA","ALA","ALA","COO-"], "SPC", [] )

        print (topology.Debug())

        with open( "../tests/data/gtop/gen_poly_ala.gtop", 'w') as top_ofstream:
            WriteGromosTopology( top_ofstream, topology, forcefield )
            


        #  topology = MakeSequence( forcefield, blueprint,\
        #        ["NH3+","ILE","VAL","GLY","GLY","GLN","GLU","CYS1","LYS","ASP","GLY",\
        #         "GLU","CYS2","PRO","TRP","GLN","ALA","LEU","LEU","ILE","ASN",\
        #         "GLU","GLU","ASN","GLU","GLY","PHE","CYS1","GLY","GLY","THR",\
        #         "ILE","LEU","SER","GLU","PHE","TYR","ILE","LEU","THR","ALA",\
        #         "ALA","HISA","CYS2","LEU","TYR","GLN","ALA","LYS","ARG","PHE",\
        #         "LYS","VAL","ARG","VAL","GLY","ASP","ARG","ASN","THR","GLU",\
        #         "GLN","GLU","GLU","GLY","GLY","GLU","ALA","VAL","HISA","GLU",\
        #         "VAL","GLU","VAL","VAL","ILE","LYS","HISB","ASN","ARG","PHE",\
        #         "THR","LYS","GLU","THR","TYR","ASP","PHE","ASP","ILE","ALA",\
        #         "VAL","LEU","ARG","LEU","LYS","THR","PRO","ILE","THR","PHE",\
        #         "ARG","MET","ASN","VAL","ALA","PRO","ALA","CYSH","LEU","PRO",\
        #         "GLU","ARG","ASP","TRP","ALA","GLU","SER","THR","LEU","MET",\
        #         "THR","GLN","LYS","THR","GLY","ILE","VAL","SER","GLY","PHE",\
        #         "GLY","ARG","THR","HISB","GLU","LYS","GLY","ARG","GLN","SER",\
        #         "THR","ARG","LEU","LYS","MET","LEU","GLU","VAL","PRO","TYR",\
        #         "VAL","ASP","ARG","ASN","SER","CYS1","LYS","LEU","SER","SER",\
        #         "SER","PHE","ILE","ILE","THR","GLN","ASN","MET","PHE","CYS2",\
        #         "ALA","GLY","TYR","ASP","THR","LYS","GLN","GLU","ASP","ALA",\
        #         "CYS1","GLN","GLY","ASP","SER","GLY","GLY","PRO","HISB","VAL",\
        #         "THR","ARG","PHE","LYS","ASP","THR","TYR","PHE","VAL","THR",\
        #         "GLY","ILE","VAL","SER","TRP","GLY","GLU","GLY","CYS2","ALA",\
        #         "ARG","LYS","GLY","LYS","TYR","GLY","ILE","TYR","THR","LYS",\
        #         "VAL","THR","ALA","PHE","LEU","LYS","TRP","ILE","ASP","ARG",\
        #         "SER","MET","LYS","THR","COO-"], "SPC", []  )

        

if __name__ == '__main__':

    main()