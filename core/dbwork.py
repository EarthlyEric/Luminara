# -*- coding: UTF-8 -*-
import pymysql
from core.json_loader import *

def guild_join(guild):
    db = pymysql.connect(
            host=mysqlhost,
            user=mysqluser,
            passwd=mysqlpasswd,
            db=mysqldb,
            port=mysqlport)

    try:
           cursor=db.cursor()

           # 執行 SQL 指令
           cursor.execute("""INSERT INTO guild_settings (guild_id, guild_name) VALUES 
           (%s, %s)""" ,(guild.id, guild.name))
    
           # 提交至 SQL
           db.commit()
    except Exception as error:
           print(error)
           db.rollback()  # 回滚
        
    db.close()

def guild_remove(guild):
    db = pymysql.connect(
            host=mysqlhost,
            user=mysqluser,
            passwd=mysqlpasswd,
            db=mysqldb,
            port=mysqlport)

    try:
           cursor=db.cursor()

           cursor.execute("DELETE FROM guild_settings WHERE guild_id='%s'",(guild.id))


           db.commit()
    except Exception as error:
           print(error)
           db.rollback() 

    db.close()