# -*- coding: UTF-8 -*-
import asyncio
import wavelink
import nextcord
from datetime import datetime
from nextcord.ext import commands
from classes import Cogs
from core.config import *
from core.utils import colors,icon

class Music(Cogs):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def connect_nodes(self):
        """連線到Lavalink節點"""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
            host="localhost",
            port=2333,
            password="1A6DCEE7A27DA826B313FBC562CD2",
            identifier="Public US Main VPS 01",
            https=False
            )

    @commands.Cog.listener()
    async def on_wavelink_track_end(self,player:wavelink.Player,track: wavelink.Track, reason):
        ctx=player.ctx
        vc: player=ctx.voice_client

        next_song = vc.queue.get()

        await vc.play(next_song)
        await ctx.send(f"現在播放下一首 {next_song.title}")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f"Node: <{node.identifier}> is ready!")

    @commands.command()
    async def play(self, ctx: commands.Context, *, track:wavelink.YouTubeTrack):
        if not ctx.author.voice:
            return await ctx.send(":x: **你尚未加任何語音頻道**",delete_after=1)
        if not ctx.voice_client:
            vc: wavelink.Player=await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player=ctx.voice_client

        await ctx.send("<a:loading:1001057291036020776> 搜尋歌曲中...",delete_after=1)

        track_url_button=nextcord.ui.Button(label="原始網址",style=nextcord.ButtonStyle.link,url="%s"%(track.uri))
        view=nextcord.ui.View()
        view.add_item(track_url_button)
        
        if vc.queue.is_empty and vc.is_connected and vc._source is None:
            await vc.play(track)

            embed=nextcord.Embed(title=":white_check_mark: 現在播放!",description="%s"% (track.uri),color=colors.green,timestamp=datetime.now())
            embed.set_thumbnail(url=track.thumbnail)
            embed.set_footer(text=f"Luminara", icon_url=icon.icon_url)

            await ctx.reply(embed=embed,view=view)
        else:
            await vc.queue.put_wait(track)

            embed=nextcord.Embed(title=":white_check_mark: 已加入播放清單!",description="%s"% (track.title),color=colors.green,timestamp=datetime.now())
            embed.set_thumbnail(url=track.thumbnail)
            embed.set_footer(text=f"Luminara", icon_url=icon.icon_url)

            await ctx.reply(embed=embed,view=view)
        vc.ctx = ctx

    @commands.command()
    async def leave(self,ctx:commands.Context):
        if not ctx.voice_client:
            embed=nextcord.Embed(title=f":no_entry: Luminara 沒有加入任何頻道。",color=colors.red,timestamp=datetime.now())
            embed.set_footer(text=f"Luminara", icon_url=icon.icon_url)
            
            return await ctx.reply

        vc: wavelink.Player=await ctx.voice_client.disconnect()
        embed=nextcord.Embed(title=f":no_entry: 已被{ctx.author.name}要求中斷連線",color=colors.red,timestamp=datetime.now())
        embed.set_footer(text=f"Luminara", icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)
        
def setup(bot):
    bot.add_cog(Music(bot))