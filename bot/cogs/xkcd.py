import random

import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import command, check, Context
from urllib.request import urlopen
from urllib.error import HTTPError
from bot.settings import CHANNEL_ID
import json

class Xkcd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def xkcd(self, ctx: Context, *, num=None):
        if num is None:
            return

        url = f"https://xkcd.com/{num}/info.0.json"
        try:
            response = urlopen(url)
        except HTTPError:
            await ctx.message.reply("xkcd not found")
            return

        response = json.loads(response.read())
        embed = Embed(title=response["title"],  url=response["link"])
        embed.set_image(url=response["img"])
        await ctx.message.reply(embed=embed)



def setup(bot):
    bot.add_cog(Xkcd(bot))
