# -*- coding: UTF-8 -*-
from configobj import ConfigObj
import os

class config():
    config=ConfigObj('config.ini')
    
    # Version Infomation.
    version=config['Info']['version']
    # Import MongoDB connection config.

    deploy=config['Deploy']
    if str(os.getenv('enable_beta', default=True))=='True':
        token=str(deploy['beta_token'])
    else:
        token=str(deploy['deploy_token'])