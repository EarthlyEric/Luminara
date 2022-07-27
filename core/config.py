# -*- coding: UTF-8 -*-
from configobj import ConfigObj
import os

class config():
    config=ConfigObj('config.ini')
    #版本資訊導入
    version=config['version']
    #MySQL 連線設定導入
    mysqlhost=str(config['mysqlhost'])
    mysqluser=config['mysqluser']
    mysqlpasswd=config['mysqlpasswd']
    mysqldb=config['mysqldb']
    mysqlport=int(config['mysqlport'])


    token=str(config['deploy_token'])