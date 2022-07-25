# -*- coding: UTF-8 -*-
from configobj import ConfigObj
import os

config=ConfigObj('config.ini')
  
  
#版本資訊導入
version=config['version']
#MySQL 連線設定導入
mysqlhost=str(config['mysqlhost'])
mysqluser=config['mysqluser']
mysqlpasswd=config['mysqlpasswd']
mysqldb=config['mysqldb']
mysqlport=int(config['mysqlport'])

if os.getenv('deploy') == None:
    token=str(config['local_token'])
elif os.getenv('deploy') =='True':
    token=str(config['deploy_token'])