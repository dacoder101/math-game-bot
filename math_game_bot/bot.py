"""Math game bot for Discord."""

import discord
from discord.ext import commands

from .commands import MathBotCommands


class MathGameBot(commands.Bot):
    """Math game bot for Discord."""

    def __init__(self, token):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.token = token

        MathBotCommands(self)

        @self.event
        async def on_ready():
            """Prints a message when the bot is ready."""

            await self.change_presence(activity=discord.Game(name="mathing"))

            print(f"Logged in as {self.user.name}")
            await self.tree.sync()

    def run_bot(self):
        """Start the bot."""
        self.run(self.token)
