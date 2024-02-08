from discord.ext import commands


class MathBotCommands(commands.Cog):
    """Command functionality for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Pong!"""
        await ctx.send("Pong!")

    def setup(self):
        """Set up the cog."""
        self.bot.add_cog(self)
