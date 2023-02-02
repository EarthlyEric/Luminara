# -*- coding: UTF-8 -*-
from configobj import ConfigObj
import os

class config():
    config=ConfigObj('config.ini')
    
    # Version Infomation.
    version=config['INFO']['version']
    # Import MongoDB connection config.

    deploy=config['Delpoy']
    if str(deploy['enable_beta'])=='True':
        token=str(deploy['beta_token'])
    else:
        token=str(deploy['deploy_token'])