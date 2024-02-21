"""Command functionality for the bot."""

from discord import Embed, Interaction


def setup_commands(bot):
    """Command functionality class for the bot."""

    @bot.tree.command(name="ping", description="Display the ping in milliseconds.")
    async def ping(interaction: Interaction):
        """Display the ping in milliseconds."""

        latency = bot.latency * 1000

        embed = Embed(
            title="Pong!",
            description=f"MathGameBot responded in {latency:.2f}ms.",
            color=0x00FF00,
        )

        await interaction.response.send_message(embed=embed)

    @bot.tree.command(
        name="server-count", description="Display the number of servers the bot is in."
    )
    async def server_count(interaction: Interaction):
        """Display the number of servers the bot is in."""

        embed = Embed(
            title="Server Count",
            description=(
                f"MathGameBot is in {len(bot.guilds)} servers!"
                if len(bot.guilds) > 1
                else f"MathGameBot is in {len(bot.guilds)} server."
            ),
            color=0x00FF00,
        )

        await interaction.response.send_message(embed=embed)

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
