import sys, os
working_dir = '.'
sys.path.insert(1, os.path.join(working_dir, 'FedFB'))
os.environ["PYTHONPATH"] = os.path.join(working_dir, 'FedFB')
from DP_run import *


# RUN BASELINE FEDAVG on ADULT DATASET
sim_dp('fedavg', 'logistic regression', 'adult')
