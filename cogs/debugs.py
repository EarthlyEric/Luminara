# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
from datetime import datetime

from classes import Cogs
from core.utils import colors, emojis,icon

class Debugs(Cogs):
    extension_location_list={
        "general":"commands",
        "management":"commands",
        "music":"commands",
        "errors":"events",
        "events":"events",
        "tasks":"events"}
    @commands.command(name="reload",description="重新載入指定的Extension")
    @commands.is_owner()
    async def reload(self,ctx,extension):
        extension_location=self.extension_location_list[f"{extension}"]
        try:
            await self.bot.reload_extension("cogs.%s.%s"%(extension_location,extension))
            print(f"[Debug][INFO] Reloaded {extension_location}.{extension}")

            embed = discord.Embed(title="%s | 重新載入中..."%(emojis.success), description="`%s` 載入成功"%(extension), color=colors.green,timestamp=datetime.now())
            embed.set_footer(text="Luminara • Debug System")
            return await ctx.send(embed=embed)
        except Exception as e:
            print("[Debug][ERROR] %s ")%(str(e))

            embed = discord.Embed(title="%s | 重新載入中..."%(emojis.errors), description="載入失敗", color=colors.red,timestamp=datetime.now())
            embed.add_field(name="原因",value="`%s`"%(e))
            embed.set_footer(text="Luminara • Debug System")
            return await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Debugs(bot))