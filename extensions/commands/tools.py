import discord
from datetime import datetime
from discord.ext import commands

from core.libs.class_define import Cogs
from core.utils import iptools

class Tools(Cogs):
    @commands.hybrid_command(name="address-lookup", description="查詢 網域 或 IP", with_app_command=True)
    async def address_lookup(self, ctx: commands.Context, *, query: str):
        embed=discord.Embed()
        embed.timestamp=datetime.now()
        embed.title=""
        if iptools.is_ipv4(query):
            return await ctx.send("這是一個 IPv4 位址")
        elif iptools.is_ipv6(query):
            return await ctx.send("這是一個 IPv6 位址")
        else:
            return await ctx.send("這是一個網域")
    
async def setup(bot):
    await bot.add_cog(Tools(bot))