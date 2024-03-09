# -*- coding: UTF-8 -*-
import discord
import wavelink
from datetime import datetime, timezone
from core.utils import colors,icon,utils,emojis
from discord.ext import commands
from typing import cast

from classes import Cogs
from core.config import config
from ui.view import *
from ui.musiccontroller import MusicController

class Music(Cogs):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            # Handle edge cases...
            return

        original: wavelink.Playable | None = payload.original
        track: wavelink.Playable = payload.track

        embed: discord.Embed = discord.Embed(title="Now Playing")
        embed.description = f"**{track.title}** by `{track.author}`"

        if track.artwork:
            embed.set_thumbnail(url=track.artwork)

        if original and original.recommended:
            embed.description += f"\n\n`This track was recommended via {track.source}`"

        if track.album.name:
            embed.add_field(name="Album", value=track.album.name)

        await player.home.send(embed=embed)

        musciController =MusicController()

        

    
    @commands.command(name='play')
    async def play(self,ctx: commands.Context, *, query: str):
        embed = discord.Embed()
        embed.set_footer(text='Luminara')
        embed.timestamp=datetime.now(timezone.utc)
        if not ctx.guild:
            embed.color=discord.Color.red()
            embed.title="%s | 無法在私人訊息中使用此命令 !" % (emojis.errors)
            return await ctx.send(embed=embed)
    
        player : wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)
        
        if not player:
            try:
                embed.color=colors.green
                embed.title="%s | 成功加入您所處的語音頻道 %s" % (emojis.success,ctx.author.voice.channel.mention)
                
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
                await ctx.send(embed=embed)
            except AttributeError:
                embed.color=discord.Color.red()
                embed.title="%s | 請先加入任一語音頻道在使用本命令" % (emojis.errors)
                return await ctx.send(embed=embed)   
            except discord.ClientException:
                embed.color=discord.Color.red()
                embed.title="%s | 未知原因，無法加入您所處的語音頻道" % (emojis.errors)
                return await ctx.send(embed=embed)
            
        player.autoplay = wavelink.AutoPlayMode.enabled

        if not hasattr(player, 'home'):
            player.home = ctx.channel
        elif player.home != ctx.channel:
            embed.color=discord.Color.red()
            embed.title="%s | 只能在 %s" % (emojis.errors,player.home.mention)
            await ctx.send(embed=embed)
        
        tracks: wavelink.Search = await wavelink.Playable.search(query)

        if not tracks:
            embed.color=discord.Color.red()
            await ctx.send(f"{ctx.author.mention} - Could not find any tracks with that query. Please try again.")
            return

        if isinstance(tracks, wavelink.Playlist):
            # tracks is a playlist...
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(f"Added the playlist **`{tracks.name}`** ({added} songs) to the queue.")
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(track)
            await ctx.send(f"Added **`{track}`** to the queue.")

        if not player.playing:
            # Play now since we aren't playing anything...
            await player.play(player.queue.get())
            

async def setup(bot):
    await bot.add_cog(Music(bot))