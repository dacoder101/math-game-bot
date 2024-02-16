"""Command functionality for the bot."""

from discord import Embed, Interaction
import discord


def setup_commands(bot):
    """Command functionality class for the bot."""

    @bot.tree.command(name="ping", description="Display the ping in milliseconds.")
    async def ping(interaction: Interaction):
        """Display the ping in milliseconds."""

        latency = bot.latency * 1000
        await interaction.response.send_message(f"Pong! {latency:.2f}ms")

    @bot.tree.command(
        name="server-count", description="Display the number of servers the bot is in."
    )
    async def server_count(interaction: Interaction):
        """Display the number of servers the bot is in."""

        message = (
            f"I'm in {len(bot.guilds)} servers"
            if len(bot.guilds) > 1
            else f"I'm in {len(bot.guilds)} server"
        )

        await interaction.response.send_message(message)

    @bot.tree.command(name="new-game", description="Start a new math game.")
    async def new_game(interaction: Interaction):
        """Start a new math game."""

        pass

    @bot.tree.command(
        name="equations", description="List the equations for the math game."
    )
    async def equation_list(interaction: Interaction):
        """List the equations for submitted into the current math game."""

        pass

    @bot.tree.command(
        name="submit-equation", description="Submit an equation for the math game."
    )
    async def submit_equation(interaction: Interaction):
        """Submit an equation for the math game."""

        pass
