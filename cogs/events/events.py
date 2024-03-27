# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
import pymongo

from core.config import *
from core.db import DBClient
from classes import Cogs

class Events(Cogs):
    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):
        """
        db=pymongo.MongoClient(config.MongoDBURI)
        db["LuminaraDB"]["guilds"].insert_one({
            "id":guild.id,
            "name":guild.name,
            "language":"zh_TW",
            "settings":{
                "welcome":{
                    "channel":None,
                    "message":None,
                    "embed":False
                },
                "leave":{
                    "channel":None,
                    "message":None,
                    "embed":False
                },
                "log":{
                    "channel":None,
                    "embed":False
                }
            }
        })
        """
        print("%s"%(guild.name))

async def setup(bot):
    await bot.add_cog(Events(bot))
