import nextcord
import lavalink
from datetime import datetime, timezone
from core.utils import colors,icon,utils,emojis
from nextcord.ext import commands
from core.classes import Cogs
from core.config import config
from ui.view import *

class Music(Cogs):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost', 7000, 'testing', 'na', 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')

def setup(bot):
    bot.add_cog(Music(bot))