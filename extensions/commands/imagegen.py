from datetime import datetime,timezone
import discord
from discord.ext import commands
from typing import Optional

from core.libs.class_define import Cogs

from core.libs.wizmodel import WizModel


class ImageGen(Cogs):
    @commands.hybrid_command(name="image-gen",description="生成圖片",with_app_command=True,catagory="AI")
    async def image_gen(self,ctx:commands.Context, prompt: str, steps: Optional[int]):
        embed = discord.Embed()
        embed.title = "圖片生成器"
        embed.description = f"**主題**: `{prompt}`"
        embed.color = discord.Color.purple()
        embed.set_footer(text="Luminara • Powered by WizModel")
        embed.timestamp=datetime.now(timezone.utc)

        async with ctx.typing():
            image = await WizModel.text2image(prompt, steps)
            image_file = discord.File(image, filename="luminara-imagegen.jpg")
            embed.set_image(url="attachment://luminara-imagegen.jpg")

        return await ctx.send(embed=embed, file=image_file)

async def setup(bot):
    await bot.add_cog(ImageGen(bot))