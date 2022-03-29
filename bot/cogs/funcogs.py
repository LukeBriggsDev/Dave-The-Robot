import discord
from discord import Embed, Member
from discord.ext.commands import Cog, command, check
import re

from typing import List

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
            text = re.search(regex, message.content).string
            image = create_wilty_image(text)
            image.save(os.path.dirname(__file__) + "/../media/temp.jpg")
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
            "worst"
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
            "https://i.imgur.com/WFfKhzg.gif",
            "https://media0.giphy.com/media/t7tGsalcWtUvNSpQ9V/200.gif?cid=82a1493b8n7rl8fb6z7uyce5k1986arkwbk2d1dv9rj9l9og&rid=200.gif&ct=g",
            "https://i.gifer.com/origin/39/3987e1a120ddcbb8c74aff00c95565e6_w200.gif",
            "https://c.tenor.com/67wn6leyK5cAAAAC/always-sunny.gif"
        ]

        if "dave" in message.content.lower() or self.bot.user in message.mentions or \
                (message.reference is not None and message.reference.resolved.author == self.bot.user):
            if await dave_mentioned(message, bad_words, response_gifs):
                return

        # Praise
        good_words = [
            "awesome",
            "best",
            "good",
            "greatest",
            "love",
            "hail",
            "brilliant",
            "fantastic",
            "amazing"
        ]

        response_gifs = [
            "https://i.pinimg.com/originals/3b/6e/3c/3b6e3c966609f0a30cc6cd1aee494f76.gif",
            "https://i.pinimg.com/originals/90/45/eb/9045ebe55d40f61aabf33d63a6ab1af6.gif",
            "https://i.pinimg.com/originals/b5/65/01/b5650194ea9262489f7a9d17ee07acae.gif",
            "https://media3.giphy.com/media/gVoBC0SuaHStq/200w.gif?cid=82a1493bjpnmz3vx2vmsbnb3ne9ywf6nsv9y2sf7gft6in7d&rid=200w.gif&ct=g",
            "https://media3.giphy.com/media/14xwAVBIYjCNhu/giphy.gif",
            "https://c.tenor.com/0Fmqcn0HH3YAAAAC/almost-famous-russel-hammon.gif"
        ]

        if "dave" in message.content.lower() or self.bot.user in message.mentions or \
                (message.reference is not None and message.reference.resolved.author == self.bot.user):
            if await dave_mentioned(message, good_words, response_gifs):
                return

        # Off and on again
        regex = re.compile(r"((anyone).*(how).*(fix))|((how).*(fix).*\?)")
        if re.search(regex, message.content.lower()):
            await message.reply("Have you tried turning it off and on again?")
            return


def setup(bot):
    bot.add_cog(FunCogs(bot))


async def dave_mentioned(message: discord.Message, word_list: List[str], response_gifs: List[str]) -> bool:
    """Dave is named, mentioned, or replied to with a word from the word_list"""
    for word in word_list:
        if word in message.content.lower():
            embed = Embed()
            embed.set_image(url=random.choice(response_gifs))
            await message.reply(embed=embed)
            return True
    return False


def create_wilty_image(text: str) -> Image:
    base_image = Image.open(os.path.dirname(__file__) + "/../media/mortimer.jpg")

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
    return new_image
