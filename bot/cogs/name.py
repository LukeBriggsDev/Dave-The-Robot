from discord.ext.commands import Cog, command, check

from bot.settings import CHANNEL_ID, SERVER_2020, SERVER_2022_CHANNEL_ID


def is_in_channel():
    async def predicate(ctx):
        member = ctx.message.author
        channel = member.guild.get_channel(
            CHANNEL_ID
        ) if member.guild.id == SERVER_2020 else member.guild.get_channel(
            SERVER_2022_CHANNEL_ID)
        return channel.id == ctx.message.channel.id

    return check(predicate)


class Name(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(
        help="Change your displayed name to your real name for this server.")
    @is_in_channel()
    async def name(self, ctx, *, new_nick=None):
        member = ctx.author
        old_nick = member.nick

        if not new_nick or not new_nick.lstrip():
            await ctx.send(
                f"You forgot to include your name after the command, {member.name}!"
            )
        else:
            new_nick = " ".join(new_nick.split())
            new_nick = new_nick[:45]

            if new_nick != old_nick:
                await member.edit(nick=new_nick)

            await ctx.send(f"Hello {new_nick}! What a beautiful name.")


def setup(bot):
    bot.add_cog(Name(bot))
