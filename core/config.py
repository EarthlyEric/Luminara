# -*- coding: UTF-8 -*-
from configobj import ConfigObj
import os

class config():
    config=ConfigObj("config.ini")
    version=config["version"]

    lavalinkHost = os.getenv("lavalinkHost")
    lavalinkPasswd = os.getenv("lavalinkPasswd")

    if str(os.getenv("betaMode", default=True))=="True":
        token=os.getenv("betaToken")
        commandPrefix="b"+os.getenv("commandPrefix")
    else:
        token=os.getenv("deployToken")
        commandPrefix=config["commandPrefix"]

    MongoDBURI=os.getenv("MongoDBURI")
    