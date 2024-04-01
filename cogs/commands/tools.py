from discord.ext import commands

from core.libs.class_define import Cogs
from core.utils import IPChecker

class Tools(Cogs):
    @commands.hybrid_command(name="address-lookup", description="查詢 網域 或 IP", with_app_command=True)
    async def address_lookup(self, ctx: commands.Context, *, query: str):
        if IPChecker.is_ipv4(query):
            await ctx.send("這是一個 IPv4 位址")
        elif IPChecker.is_ipv6(query):
            await ctx.send("這是一個 IPv6 位址")
        else:
            await ctx.send("這是一個網域")
    
async def setup(bot):
    await bot.add_cog(Tools(bot))