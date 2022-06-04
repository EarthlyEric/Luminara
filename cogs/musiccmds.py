import wavelink
import json
from discord.ext import commands
from core.classes import CogTop
from core.config import *
from core.lib  import *


class Music(CogTop):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Lavalink nodes."""
        await self.bot.wait_until_ready()
        
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lava.link',
            port= 80,
            password='anything as a password',
            identifier='Public EU Main 01',
            region='eu_west',
            )
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lavalink.oops.wtf',
            port= 2000,
            password='www.freelavalink.ga',
            identifier='Public Asia Main 01',
            region='singapore',
            )
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lavalink.darrenofficial.com',
            port= 80,
            password='anything as a password',
            identifier='Public US Main 01',
            region='us_east',
            )



    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        """Play a song with the given search query.
        If not connected, connect to our voice channel.
        """
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.play(search)

def setup(bot):
    bot.add_cog(Music(bot))