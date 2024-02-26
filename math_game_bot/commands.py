"""Command functionality for the bot."""

from discord import Embed, Interaction
from discord import app_commands

from .math_game import MathGame
from .validate import ValidateIntegers, ValidateOperators


game = None


def setup_commands(bot):
    """Command functionality class for the bot."""

    @bot.tree.command(name="ping", description="Display the ping in milliseconds.")
    async def ping(interaction: Interaction):
        """Display the ping in milliseconds."""

        latency = bot.latency * 1000

        await interaction.response.send_message(
            embed=generate_embed("Pong!", f"MathGameBot responded in {latency:.2f}ms.")
        )

    @bot.tree.command(
        name="server-count", description="Display the number of servers the bot is in."
    )
    async def server_count(interaction: Interaction):
        """Display the number of servers the bot is in."""

        await interaction.response.send_message(
            embed=generate_embed(
                "Server Count",
                (
                    f"MathGameBot is in {len(bot.guilds)} servers!"
                    if len(bot.guilds) > 1
                    else f"MathGameBot is in {len(bot.guilds)} server."
                ),
            )
        )

    @bot.tree.command(name="new-game", description="Start a new math game.")
    @app_commands.describe(
        integers="Enter the the numbers range to use in the game.",
        game_max="Enter the maximum number of equations for the game. The default is 20.",
        disallowed_operations="Enter the disallowed operations for the game. If no operations are listed, all operations are allowed.",
    )
    async def new_game(
        interaction: Interaction,
        integers: str,
        game_max: int = 20,
        disallowed_operations: str = None,
    ):
        """Start a new math game."""

        global game
        game = MathGame(
            ValidateIntegers(integers).validate(),
            game_max,
            (
                ValidateOperators(disallowed_operations).validate()
                if disallowed_operations
                else None
            ),
        )

        await interaction.response.send_message(
            embed=generate_embed("New Game", "A new game has been started.")
        )

    @bot.tree.command(name="help", description="Display the help message.")
    async def help(interaction: Interaction):
        """Display the help message."""

        await interaction.response.send_message(
            embed=generate_embed(
                "Help",
                "Use the following commands to interact with the bot:\n"
                "`/ping` - Display the ping in milliseconds.\n"
                "`/server-count` - Display the number of servers the bot is in.\n"
                "`/new-game` - Start a new math game.\n"
                "`/game-info` - Display the game info.\n"
                "`/equations` - List the equations for the math game.\n"
                "`/submit-equation` - Submit an equation for the math game.\n"
                "`/remove-equation` - Remove an equation from the math game.",
            )
        )

    @bot.tree.command(name="game-info", description="Display the game info.")
    async def game_info(interaction: Interaction):
        """Display the game info."""

        if game is not None:
            await interaction.response.send_message(
                embed=generate_embed("Game Info", str(game))
            )
        else:
            await interaction.response.send_message(
                embed=game_isnt_started(), ephemeral=True
            )

    @bot.tree.command(
        name="equations", description="List the equations for the math game."
    )
    async def equation_list(interaction: Interaction):
        """List the equations for submitted into the current math game."""

        if game is not None:
            await interaction.response.send_message(
                embed=generate_embed("Equations", game.get_equations())
            )

        else:
            await interaction.response.send_message(
                embed=game_isnt_started(),
                ephemeral=True,
            )

    @bot.tree.command(
        name="submit-equation", description="Submit an equation for the math game."
    )
    @app_commands.describe(equation="Enter the equation to submit.")
    async def submit_equation(interaction: Interaction, equation: str):
        """Submit an equation for the math game."""

        if game is not None:
            try:
                game.submit_equation(equation)

                await interaction.response.send_message(
                    embed=generate_embed(
                        "Submit Equation", "The equation has been submitted."
                    )
                )

            except Exception as e:
                await interaction.response.send_message(
                    embed=generate_embed("Submit Equation", str(e)),
                    ephemeral=True,
                )

        else:
            await interaction.response.send_message(
                embed=game_isnt_started(),
                ephemeral=True,
            )

    @bot.tree.command(
        name="remove-equation", description="Remove an equation from the math game."
    )
    @app_commands.describe(result="Enter the result of the equation to remove.")
    async def remove_equation(interaction: Interaction, result: int):
        """Remove an equation from the math game."""

        if game is not None:
            game.remove_equation(result)

            await interaction.response.send_message(
                embed=generate_embed(
                    "Remove Equation", "The equation has been removed."
                )
            )

        else:
            await interaction.response.send_message(
                embed=game_isnt_started(),
                ephemeral=True,
            )


def generate_embed(title, content, color=0x00FF00):
    """Generate an embed message with the given content and color."""

    return Embed(
        title=title,
        description=content,
        color=color,
    )


def game_isnt_started():
    """Return a message indicating that the game isn't started."""

    return generate_embed(
        "Game Info",
        "No game has been started. Use `/new-game` to start a new game.",
    )
