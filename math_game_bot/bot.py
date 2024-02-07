"""Math game bot for Discord."""

import os
import discord
from discord.ext import commands


class MathGameBot(commands.Bot):
    """Math game bot for Discord."""

    def __init__(self, token):
        super().__init__(command_prefix="!", intents=discord.Intents.default())
        self.token = token

    async def on_ready(self):
        """Prints a message when the bot is ready."""
        print(f"Logged in as {self.user.name}")

    @commands.command()
    async def ping(self, ctx):
        """Measures the bot's latency."""
        latency = round(self.latency * 1000)
        await ctx.send(f"Pong! Latency: {latency}ms")

    @commands.command()
    async def servers(self, ctx):
        """Prints the number of servers the bot is in."""
        servers = len(self.guilds)
        await ctx.send(f"The bot is in {servers} servers.")

    def run_bot(self):
        """Start the bot."""
        self.run(self.token)


TOKEN = os.environ.get("MATH_BOT_TOKEN")
bot = MathGameBot(TOKEN)
bot.run_bot()
