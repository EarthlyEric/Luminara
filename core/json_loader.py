# -*- coding: UTF-8 -*-
import json

with open('./settings.json','r') as jsettings:
  
  jsettingsbake=json.load(jsettings)
  #版本資訊導入
  printversion=jsettingsbake['printversion']
  #//MySQL 設定導入
  fmysqlhost=jsettingsbake['mysqlhost']
  mysqlhost=str(fmysqlhost)

  mysqluser=jsettingsbake['mysqluser']

  mysqlpasswd=jsettingsbake['mysqlpasswd']

  mysqldb=jsettingsbake['mysqldb']

  fmysqlport=jsettingsbake['mysqlport']
  mysqlport=int(fmysqlport)




with open('./token.json','r') as jtoken:
    jtokenbake=json.load(jtoken)
    #Token 設定導入
    token=jtokenbake['token']