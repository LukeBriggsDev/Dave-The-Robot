import discord
from discord import Embed, Member
from discord.ext.commands import Cog, command, check
import re
from bot.settings import CHANNEL_ID, FIELDS
from PIL import Image, ImageDraw, ImageFont
import os
import random

class FunCogs(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        # League of Gentlemen Localhost
        regex = re.compile(r"(localhost)|(127.0.0.1)|(local host)")
        if re.search(regex, message.content.lower()):
            embed = Embed()
            embed.set_image(url="https://c.tenor.com/sSBdT5ha3GUAAAAC/league-of-gentlemen-local-shop.gif")
            await message.reply("That is a localhost for local people, we'll have no servers there", embed=embed)
            return

        # WILTY
        regex = re.compile(r"(I once)[^.\n]*", re.IGNORECASE)
        if re.search(regex, message.content.lower()):
            base_image = Image.open(os.path.dirname(__file__) + "/../media/mortimer.jpg")

            text = re.search(regex, message.content).string
            font_size = 1
            font = ImageFont.truetype(os.path.dirname(__file__) + "/../media/texgyreheros-regular.otf", font_size)
            while font.getsize(text)[0] < base_image.width * 0.9:
                font_size += 1
                font = ImageFont.truetype(os.path.dirname(__file__) + "/../media/texgyreheros-regular.otf", font_size)

            new_image = Image.new("RGB",
                                  (base_image.width,
                                   base_image.height + font.getsize(text)[1] + 20),
                                  color=(255, 255, 255))
            new_image.paste(base_image)
            draw = ImageDraw.Draw(new_image)

            draw.text((10, base_image.height + 10), text, (0, 0, 0), font=font)
            new_image.save(os.path.dirname(__file__) + "/../media/temp.jpg")
            await message.reply(file=discord.File(os.path.dirname(__file__) + "/../media/temp.jpg"))
            return

        # insult
        bad_words = [
            "shut up",
            "hate",
            "go away",
            "piss off",
            "fuck off",
            "fuck",
        ]

        response_gifs = [
            "http://i.imgur.com/rT7bTDa.gif",
            "https://i.pinimg.com/originals/2e/8f/a2/2e8fa2ced89852c4a7aeba11e17fcf77.gif",
            "https://i.imgur.com/Lpt8LxL.gif?noredirect",
            "https://img.gifglobe.com/grabs/blackbooks/S02E06/gif/AjbRfqjmgG5P.gif",
            "https://i.pinimg.com/originals/2d/6f/c3/2d6fc3cd5616718f89f21f2a95ff0efc.gif",
            "https://c.tenor.com/pgg-9i83eLMAAAAd/black-books.gif",
            "https://media2.giphy.com/media/vNNoOAV7OUqsg/giphy.gif",
            "https://media0.giphy.com/media/79GPUDKNCXBJu/giphy.gif",
            "https://i.imgur.com/WFfKhzg.gif"
        ]
        if "dave" in message.content.lower() or self.bot.user in message.mentions or \
                (message.reference is not None and message.reference.resolved.author == self.bot.user):
            for word in bad_words:
                if word in message.content.lower():
                    embed = Embed()
                    embed.set_image(url=random.choice(response_gifs))
                    await message.reply(embed=embed)
                    return

def setup(bot):
    bot.add_cog(FunCogs(bot))
