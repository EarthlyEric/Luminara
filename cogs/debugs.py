# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
from datetime import datetime

from classes import Cogs
from core.utils import colors, emojis, icon, extension_path

class Debugs(Cogs):
    
    @commands.command(name="reload",description="重新載入指定的Extension")
    @commands.is_owner()
    async def reload(self,ctx,extension):
        extension_location=extension_path[f"{extension}"]

        embed=discord.Embed(timestamp=datetime.now())
        embed.set_footer(text="Luminara • Debug System")
        try:
            await self.bot.reload_extension("cogs.%s.%s"%(extension_location,extension))
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
async def setup(bot):
    await bot.add_cog(Debugs(bot))