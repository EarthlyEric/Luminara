# -*- coding: UTF-8 -*-
from configobj import ConfigObj

config=ConfigObj('config.ini')
  
  
#版本資訊導入
printversion=config['printversion']
#//MySQL 設定導入
fmysqlhost=config['mysqlhost']
mysqlhost=str(fmysqlhost)

mysqluser=config['mysqluser']

mysqlpasswd=config['mysqlpasswd']

mysqldb=config['mysqldb']

fmysqlport=config['mysqlport']
mysqlport=int(fmysqlport)

token=str(config['token'])