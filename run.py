"""Execute the bot."""

import os

from math_game_bot.bot import MathGameBot


def run_bot():
    """Start the bot."""

    TOKEN = os.environ.get("MATH_BOT_TOKEN")
    bot = MathGameBot(TOKEN)
    bot.run_bot()


if __name__ == "__main__":
    run_bot()
