import pymysql
from core.config import config

def connect():
       db=pymysql.connect(
            host=config.mysqlhost,
            user=config.mysqluser,
            passwd=config.mysqlpasswd,
            db=config.mysqldb,
            port=config.mysqlport)
       return db

db=connect()