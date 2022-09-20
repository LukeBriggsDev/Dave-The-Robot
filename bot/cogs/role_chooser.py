import sys

from discord.ext.commands import Cog, command, check
from discord.utils import find
from typing import List
from bot.settings import CHANNEL_ID, FIELDS, TOPICS, STAGE_3_MODULES, PRONOUNS, SERVER_2020, SERVER_2022_CHANNEL_ID
from bot.cogs.name import Name


def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id

    return check(predicate)


def is_in_channel():
    async def predicate(ctx):
        member = ctx.message.author
        channel = member.guild.get_channel(
            CHANNEL_ID
        ) if member.guild.id == SERVER_2020 else member.guild.get_channel(
            SERVER_2022_CHANNEL_ID)
        return channel.id == ctx.message.channel.id

    return check(predicate)


class RoleChooser(Cog, name="Choose Roles"):
    """List of commands to set roles for various topics and modules"""
    def __init__(self, bot):
        self.bot = bot

    def _common(self, list1, list2):
        return list(set(list1) & set(list2))

    async def change_role(self, ctx, rolename: str, role_type: str,
                          pos_roles: List[str], max_num: int):
        member = ctx.author
        name = member.nick or member.name

        if not rolename:
            await ctx.send(
                f"You forgot to provide a {role_type} name after the command, {name}!"
            )
            return

        if rolename.lower() not in pos_roles:
            await ctx.send(f"Role change failed, {name}."
                           "You are only allowed the roles below\n"
                           "```\n" + '\n'.join(pos_roles) + "\n```")
            return

        author_roles = [
            role.name.lower() for role in ctx.author.roles
            if role.name != "@everyone"
        ]
        common_roles = self._common(author_roles, pos_roles)

        if rolename.lower() in common_roles:
            await ctx.send(f"You already have that role, {name}!")
            return

        role = find(
            lambda r: r.name.lower() == rolename.lower(),
            member.guild.roles,
        )

        if common_roles:
            role_objs = [
                find(
                    lambda r: r.name.lower() == cr_name,
                    member.guild.roles,
                ) for cr_name in common_roles
            ]
            if len(role_objs) >= max_num:
                await member.remove_roles(*role_objs)

        await member.add_roles(role)
        await ctx.send(f"Successfully assigned to {role.name}, {name}!")

    @command(help="Select your field", usage=f"[{'|'.join(FIELDS)}]")
    @is_in_channel()
    async def field(self, ctx, *, rolename=None):
        await self.change_role(ctx,
                               rolename,
                               "field",
                               pos_roles=FIELDS,
                               max_num=1)

    @command(help="Select your CSC2034 topic", usage=f"[{'|'.join(TOPICS)}]")
    @is_in_guild(SERVER_2020)
    @is_in_channel()
    async def topic(self, ctx, *, rolename=None):
        await self.change_role(ctx,
                               rolename,
                               "topics",
                               pos_roles=TOPICS,
                               max_num=1)

    @command(help="Select your Stage 3 modules",
             usage='\n'.join(STAGE_3_MODULES))
    @is_in_guild(SERVER_2020)
    @is_in_channel()
    async def stage3(self, ctx, *, rolename=None):
        await self.change_role(
            ctx,
            rolename,
            "Stage 3 Module",
            pos_roles=[x.split(' ')[0] for x in STAGE_3_MODULES],
            max_num=4)

    @command(help="Preferred Pronouns", usage='\n'.join(PRONOUNS))
    @is_in_channel()
    async def pronoun(self, ctx, *, rolename=None):
        await self.change_role(ctx,
                               rolename,
                               "Preferred Pronouns",
                               pos_roles=PRONOUNS,
                               max_num=1)
        member = ctx.author
        old_nick = member.nick
        if old_nick is None:
            old_nick = member.name
        old_pronoun = None
        for pronoun in PRONOUNS:
            if pronoun in old_nick:
                old_pronoun = pronoun
        if old_pronoun is None:
            new_nick = f"{old_nick} ({rolename})"
        else:
            new_nick = old_nick.replace(old_pronoun, rolename)
        print(new_nick)
        await member.edit(nick=new_nick)


def setup(bot):
    bot.add_cog(RoleChooser(bot))
