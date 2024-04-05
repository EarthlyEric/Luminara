# -*- coding: UTF-8 -*-
from typing import Optional
import typing
import discord
from discord.ext import commands
from datetime import datetime

from core.libs.class_define import Cogs
from core.utils import colors, emojis, icon, extension_path

class Debugs(Cogs):
    
    @commands.hybrid_command(name="reload",description="重新載入指定的 Extension !",with_app_command=True)
    @commands.is_owner()
    async def reload(self, ctx:commands.Context, extension:str):
        if not extension_path[f"{extension}"]:
            return await ctx.send(f"Extension `{extension}` not found.")

        extension_location=extension_path[f"{extension}"]

        embed=discord.Embed(timestamp=datetime.now())
        embed.set_footer(text="Luminara • Debug System")
        try:
            await self.bot.reload_extension("extensions.%s.%s"%(extension_location,extension))
            print(f"[Debug][INFO] Reloaded {extension_location}.{extension}")

            embed.title=f"{emojis.success} | 重新載入中..."
            embed.description=f"`{extension}` 載入成功"
            embed.color=colors.green

            return await ctx.send(embed=embed)
        except Exception as e:
            print(f"[Debug][ERROR] {e}")

            embed.title=f"{emojis.errors} | 重新載入中..."
            embed.description="載入失敗"
            embed.color=colors.red
            embed.add_field(name="原因", value=f"`{e}`")
            
            return await ctx.send(embed=embed)
    
    @reload.autocomplete("extension")
    async def reload_autocomplete(self, ctx:commands.Context, current:str) -> typing.List[discord.app_commands.Choice]:
        return [discord.app_commands.Choice(name="general", value="general"),
                discord.app_commands.Choice(name="management", value="management"),
                discord.app_commands.Choice(name="music", value="music"),
                discord.app_commands.Choice(name="errors", value="errors"),
                discord.app_commands.Choice(name="events", value="events"),
                discord.app_commands.Choice(name="tasks", value="tasks"),
                discord.app_commands.Choice(name="imagegen", value="imagegen"),
                discord.app_commands.Choice(name="funs", value="funs"),
                discord.app_commands.Choice(name="copilot", value="copilot"),
                discord.app_commands.Choice(name="tools", value="tools")]
    
    @commands.hybrid_command(name="sync",description="同步所有的Slash Commands",with_app_command=True)
    @commands.is_owner()
    async def sync(self, ctx:commands.Context, type:str, id:Optional[int]):
        embed=discord.Embed(timestamp=datetime.now())
        embed.set_footer(text="Luminara • Debug System")
        if not id:
            id=ctx.guild.id
            
        guild=self.bot.get_guild(id)
        try:
            if type=="guild":
                await self.bot.tree.copy_global_to(guild=guild)
            elif type=="global":
                await self.bot.tree.sync()
            print("[Debug][INFO] Synced all Slash Commands")
            embed.title=f"{emojis.success} | 同步中..."
            embed.description="同步成功"
            embed.color=colors.green

            return await ctx.send(embed=embed)
        except Exception as e:
            print(f"[Debug][ERROR] {e}")

            embed.title=f"{emojis.errors} | 同步中..."
            embed.description="同步失敗"
            embed.color=colors.red
            embed.add_field(name="原因", value=f"`{e}`")
            
            return await ctx.send(embed=embed)
    
    @sync.autocomplete("type")
    async def sync_autocomplete(self, ctx:commands.Context, current:str) -> typing.List[discord.app_commands.Choice]:
        return [discord.app_commands.Choice(name="guild", value="guild"),
                discord.app_commands.Choice(name="global", value="global")]
        
async def setup(bot):
    await bot.add_cog(Debugs(bot))