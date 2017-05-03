# -*- coding: utf-8 -*-

"""
file: settings.py

lie_atb module wide settings
"""

SETTINGS = {
    'atb_url': 'https://atb.uq.edu.au',
    'atb_api_token': '53A4C6BE1CB66913D3A658AD7932B4DD',
    'atb_api_debug': False,
    'atb_api_timeout': 45,
    'atb_forcefield_version': ['53A6','54A7']
}

ALLOWED_QUERY_KEYS = ['iupac','inchi','common_name','formula','rnme',
                      'maximum_qm_level','curation_trust','is_finished',
                      'user_label','tag','any','match_partial','moltype',
                      'max_atoms','min_atoms','has_pdb_hetId']

SUPPORTED_STRUCTURE_FILE_FORMATS = {
    'pqr_allatom_optimised':'cry',
    'pqr_allatom_unoptimised':'cry',
    'pqr_uniatom_optimised':'cry',
    'pqr_uniatom_unoptimised':'cry',
    'pdb_allatom_optimised':'top',
    'pdb_allatom_unoptimised':'top',
    'pdb_uniatom_optimised':'top',
    'pdb_uniatom_unoptimised':'top',
    'cif_allatom':'cry',
    'cif_allatom_extended':'cry',
    'cif_uniatom':'cry',
    'cif_uniatom_extended':'cry'
}

SUPPORTED_TOPOLOGY_FILE_FORMATS = {
    'lammps_allatom_optimised':'lammps_allatom_optimised.lt',
    'lammps_allatom_unoptimised':'lammps_allatom_unoptimised.lt',
    'lammps_uniatom_optimised':'lammps_uniatom_optimised.lt',
    'lammps_uniatom_unoptimised':'lammps_uniatom_unoptimised.lt',
    'mtb96_allatom':'mtb96_allatom',
    'mtb96_uniatom':'mtb96_uniatom',
    'mtb_allatom':'mtb_allatom',
    'mtb_uniatom':'mtb_uniatom',
    'cns_allatom_top':'cns_allatom_top',
    'cns_allatom_param':'cns_allatom_param',
    'cns_uniatom_top':'cns_uniatom_top',
    'cns_uniatom_param':'cns_uniatom_param',
    'rtp_allatom':'rtp_allatom',
    'rtp_uniatom':'rtp_uniatom'
}