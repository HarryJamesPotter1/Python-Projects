import discord 
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = discord.Embed(
            description="**Reaction Poll**\nCreate a reaction poll by typing `+poll *your message*`. Poll Bot will automatically add the reactions 👍, 👎, and 🤷.\nCreate a reaction poll with multiple options by typing `+poll {title} [Option1] [Option2] [Option3]`.\n"
            + "\n**Other Commands**\n+invite\n\n**Still Have Questions?**\nAsk Kushal"
            + "\n",
            colour=0x83BAE3,
        )

        self.invite_message = discord.Embed(
            description="Invite Poll Bot to your server: <https://discord.com/api/oauth2/authorize?client_id=928415755358306325&permissions=449898335296&scope=bot>",
            colour=0x83BAE3,
        )

    @commands.command(name="help")
    @commands.cooldown(2,60,BucketType.user) 
    async def help(self, ctx):
        await ctx.message.channel.send(embed=self.help_message)

    @commands.command(name="invite")
    @commands.cooldown(2,60,BucketType.user) 
    async def invite(self, ctx):
        await ctx.message.channel.send(embed=self.invite_message)

    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)

    @invite.error
    async def invite_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)

def setup(bot):
    bot.add_cog(Meta(bot))
