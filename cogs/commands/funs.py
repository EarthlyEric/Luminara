import discord
from discord.ext import commands

from core.libs.class_define import Cogs
from core.libs.bullshit import BullshitTextGen

class Funs(Cogs):
    @commands.hybrid_command(name="bullshit", description="唬爛文生成器", with_app_command=True)
    async def test(self, ctx: commands.Context, topic:str, length:int):
        text_gen = BullshitTextGen.generate(topic, length)
        return await ctx.reply(text_gen)
    
async def setup(bot):
    await bot.add_cog(Funs(bot))