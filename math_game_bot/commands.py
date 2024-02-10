"""Command functionality for the bot."""

import discord
from discord.ext import commands


class MathBotCommands:
    """Command functionality for the bot."""

    def __init__(self, bot: commands.Bot):
        @bot.tree.command(name="ping")
        async def ping(interaction: discord.Interaction):
            """Display the ping in milliseconds."""

            latency = bot.latency * 1000
            await interaction.response.send_message(f"Pong! {latency:.2f}ms")

        @bot.tree.command(name="server-count")
        async def server_count(interaction: discord.Interaction):
            """Display the number of servers the bot is in."""

            message = (
                f"I'm in {len(bot.guilds)} servers"
                if len(bot.guilds) > 1
                else f"I'm in {len(bot.guilds)} server"
            )

            await interaction.response.send_message(message)
