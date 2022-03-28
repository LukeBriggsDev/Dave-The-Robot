from discord.ext.commands import Cog, command, check

from bot.settings import CHANNEL_ID


class Name(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(
        help="Change your displayed name to your real name for this server."
    )
    @check(lambda ctx: ctx.message.channel.id == CHANNEL_ID)
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