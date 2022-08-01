import operator
import wavelink
import nextcord
from core.icon import icon
from nextcord.ext import commands
from core.classes import Cogs
from core.config import *
from core.lib  import *
from core.embed_color import colors

class Music(Cogs):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot:commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """連線到Lavalink節點"""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
            host='us01.lavalink.reload-dev.ml',
            port=443,
            password='1A6DCEE7A27DA826B313FBC562CD2',
            identifier='Public US Main VPS 01',
            https=True,
            )

        await wavelink.NodePool.create_node(bot=self.bot,
            host='51.161.130.134',
            port=10414,
            password='1A6DCEE7A27DA826B313FBC562CD2',
            identifier='Public Asia Main VPS 01',
            )
        
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lava.link',
            port= 80,
            password='anything as a password',
            identifier='Public EU Main 01',
            )
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lavalink.oops.wtf',
            port= 2000,
            password='www.freelavalink.ga',
            identifier='Public Asia Main 01',
            )
    @commands.Cog.listener()
    async def on_wavelink_track_end(self,player:wavelink.Player,track: wavelink.Track, reason):
        ctx = player.ctx
        vc: player = ctx.voice_client

        next_song = vc.queue.get()

        await vc.play(next_song)
        await ctx.send(f"現在播放下一首 {next_song.title}")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, track:wavelink.YouTubeTrack):
        await ctx.send('<a:loading:1001057291036020776> 搜尋歌曲中...',delete_after=3)

        if not ctx.voice_client:
            vc: wavelink.Player=await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player=ctx.voice_client

        if vc.queue.is_empty and operator.not_(vc.is_playing):
            embed=nextcord.Embed(title=':white_check_mark: 現在播放 !',description='%s'% (track.title),color=colors.green)
            embed.set_thumbnail(url=track.thumbnail)
            embed.set_footer(text=f'Lost', icon_url=icon.icon_url)

            await ctx.reply(embed=embed)

            await vc.play(track)
        else:
            await vc.queue.put_wait(track)




        



    @commands.command()
    async def leave(self,ctx:commands.Context):
        if not ctx.voice_client:
            embed=nextcord.Embed(title=f':no_entry: Lost 沒有加入任何頻道。',color=colors.red)
            embed.set_footer(text=f'Lost', icon_url=bot.icon_url)
            
            return await ctx.reply

        vc: wavelink.Player=await ctx.voice_client.disconnect()
        embed=nextcord.Embed(title=f':no_entry: 已被{ctx.author.name}要求中斷連線',color=colors.red)
        embed.set_footer(text=f'Lost', icon_url=bot.icon_url)

        return await ctx.reply(embed=embed)
    

def setup(bot):
    bot.add_cog(Music(bot))