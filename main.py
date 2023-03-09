from bot import settings
from bot.bot import Dave
from discord import Intents
from dotenv  import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    bot = Dave(command_prefix="!", intents=Intents.all())

    bot.load_extension("bot.cogs.role_chooser")
    bot.load_extension("bot.cogs.name")
    bot.load_extension("bot.cogs.greetings")
    bot.load_extension("bot.cogs.funcogs")
    bot.load_extension("bot.cogs.xkcd")
    bot.load_extension("bot.cogs.tweet")
    print("Bot loaded")
    bot.run(settings.CLIENT_TOKEN)
