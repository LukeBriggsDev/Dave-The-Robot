from bot import settings
from bot.bot import Dave
from discord import Intents

if __name__ == "__main__":
    bot = Dave(command_prefix="!", intents=Intents.all())

    bot.load_extension("bot.cogs.role_chooser")
    bot.load_extension("bot.cogs.name")
    bot.load_extension("bot.cogs.greetings")
    bot.load_extension("bot.cogs.funcogs")
    print("Bot loaded")
    bot.run(settings.CLIENT_TOKEN)

