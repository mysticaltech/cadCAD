import os, dill

name = "cadCAD"
configs = []

sys_job_metrics = None
# sys_job_metrics = {'sim_id': 10, 'subset_id': 0, 'run': 10}
remote_dict = {'metrics': sys_job_metrics}

if os.name == 'nt':
    dill.settings['recurse'] = True

logo = r'''
                  ___________    ____
  ________ __ ___/ / ____/   |  / __ \
 / ___/ __` / __  / /   / /| | / / / /
/ /__/ /_/ / /_/ / /___/ ___ |/ /_/ /
\___/\__,_/\__,_/\____/_/  |_/_____/
by cadCAD
'''
