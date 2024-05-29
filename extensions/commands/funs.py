from discord.ext import commands

from core.libs.bot import Cogs
from core.libs.bullshit import BullshitTextGen

class Funs(Cogs):
    @commands.hybrid_command(name="bullshit", description="唬爛文生成器", with_app_command=True)
    async def test(self, ctx: commands.Context, topic:str, length:int):
        text_gen = BullshitTextGen()
        text=text_gen.generate(param_topic=topic, param_min_length=length)
        await ctx.reply(text)
    
async def setup(bot):
    await bot.add_cog(Funs(bot))