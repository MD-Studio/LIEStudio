# -*- coding: utf-8 -*-

# from lie_md.gromacs_gromit import gromit_cmd
import cerise_client.service as cc


def create_cerise_config(workdir, session):
    """
    Configuration to run MD jobs.
    """
    cerise_config = {
        'workdir': workdir,
        'docker_name':
        'cerise-mdstudio-das5-myuser',
        'docker_image':
        'mdstudio/cerise-mdstudio-das5:develop',
        'port': 29593,
        "task_id": session["task_id"]}

    return cerise_config


def call_cerise_gromacs(gromacs_config, cerise_config):
    """
    Use cerise to run gromacs in a remote cluster, see:
    http://cerise-client.readthedocs.io/en/latest/
    """
    pass
    # srv, cerise_config = create_service(cerise_config)

    # # Start service
    # cc.start_managed_service(srv)

    # # Create jobs
    # job = create_job(srv, gromacs_config, cerise_config)

    # # run the job in the remote
    # run_job(job, srv, cerise_config)


def create_service(config):
    """
    Create a Cerise service if one is not already running.
    """
    srv_data = config.get('service_dict', None)
    if srv_data is not None:
        srv = cc.service_from_dict(srv_data)
    else:
        srv = cc.require_managed_service(
            config['docker_name'],
            config['port'],
            config['docker_image'],
            config['user_name'],
            config['password'])

        # Update config
        config['service_dict'] = cc.service_to_dict(srv)

    return srv, config


def create_job(srv, gromacs_config, cerise_config):
    """
    Create a Cerise job and set gromacs
    """
    job_name = 'job_{}'.format(cerise_config['task_id'])
    job = srv.create_job(job_name)

    # copy_files to remote worker
    files = ['protein_pdb', 'ligand_pdb', 'ligand_itp']
    for name in files:
        job.add_input_file(name, gromacs_config[name])

    return job


def run_job(job, srv, cerise_config):
    pass


def copy_files_to_remote(srv, gromacs_config):
    """
    Tell to Cerise which files to copy.
    """
    pass


def retrieve_energies(workdir):
    """
    """
    pass

        # gmxRun = gromit_cmd(gromacs_config)

        # if protein_file:
        #     gmxRun += '-f {0} '.format(os.path.basename(protdsc))

        # if ligand_file:
        #     gmxRun += '-l {0},{1} '.format(
        #         os.path.basename(ligdsc), os.path.basename(results['itp']))

        # # Prepaire post analysis (energy extraction)
        # eneRun = 'python getEnergies.py -gmxrc {0} -ene -o ligand.ene'.format(GMXRC)

        # # write executable
        # with open('run_md.sh', 'w') as outFile:
        #     outFile.write("{0}\n".format(gmxRun))
        #     outFile.write("{0}\n".format(eneRun))
