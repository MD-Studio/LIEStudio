# -*- coding: utf-8 -*-

"""
lie_docking module wide settings containing settings
for each of the supported docking methods.
"""

SETTINGS = {
    'plants': {
        'exec_path': '{system.app_path}/bin/plants_{system.platform}',
        'scoring_function': 'chemplp', #plp, plp95 or chemplp
        'outside_binding_site_penalty': 50.0,
        'enable_sulphur_acceptors': 0,
        'ligand_intra_score': 'clash2',
        'chemplp_clash_include_14': 1,
        'chemplp_clash_include_HH': 0,
        'plp_steric_e': -0.4,
        'plp_burpolar_e': -0.05,
        'plp_hbond_e': -2.0,
        'plp_metal_e': -4.0,
        'plp_repulsive_weight': 0.5,
        'plp_tors_weight': 1.0,
        'chemplp_weak_cho': 1,
        'chemplp_charged_hb_weight': 2.0,
        'chemplp_charged_metal_weight': 2.0,
        'chemplp_hbond_weight': -3.0,
        'chemplp_hbond_cho_weight': -3.0,
        'chemplp_metal_weight': -6.0,
        'chemplp_plp_weight': 1.0,
        'chemplp_plp_steric_e': -0.4,
        'chemplp_plp_burpolar_e': -0.1,
        'chemplp_plp_hbond_e': -1.0,
        'chemplp_plp_metal_e': -1.0,
        'chemplp_plp_repulsive_weight': 1.0,
        'chemplp_tors_weight': 2.0,
        'chemplp_lipo_weight': 0.0,
        'chemplp_intercept_weight': -20.0,
        'rescore_mode': 'simplex',
        'search_speed': 'speed1',
        'protein_file': 'protein.mol2',
        'ligand_file': 'ligand.mol2',
        'output_dir': '.',
        'write_multi_mol2': 0,
        'flip_amide_bonds': 1,
        'flip_planar_n': 1,
        'flip_ring_corners': 0,
        'force_flipped_bonds_planarity': 0,
        'force_planar_bond_rotation': 1,
        'bindingsite_center': [0.0,0.0,0.0],
        'bindingsite_radius': 12,
        'cluster_structures': 50,
        'cluster_rmsd': 1.0,
        'write_ranking_links': 0,
        'write_protein_bindingsite': 0,
        'write_protein_conformations': 0,
        'write_merged_protein': 0,
        'write_merged_ligand': 0,
        'write_merged_water': 0,
        'write_per_atom_scores': 0,
        'merge_multi_conf_output': 0
    }    
}