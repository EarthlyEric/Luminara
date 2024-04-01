from discord.ext import commands

from core.libs.class_define import Cogs

class Tools(Cogs):
    @commands.hybrid_command(name="address-lookup", description="查詢 網域 或 IP", with_app_command=True)
    async def address_lookup(self, ctx: commands.Context, *, query: str):
        pass
    
async def setup(bot):
    await bot.add_cog(Tools(bot))