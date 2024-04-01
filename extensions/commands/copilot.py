from discord.ext import commands
from sydney import SydneyClient
from discord.ext import commands

from core.libs.class_define import Cogs

class Copilot(Cogs):
    @commands.hybrid_command(name="ask", description="向AI詢問一個問題", with_app_command=True)
    async def ask(self, ctx: commands.Context, question:str):
        async with ctx.typing():
            async with SydneyClient() as client:
                response = await client.ask_stream(question)
                return await ctx.reply(response)
    
    
    
async def setup(bot):
    await bot.add_cog(Copilot(bot))