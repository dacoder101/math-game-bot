"""Execute the bot."""

import os

from dotenv import load_dotenv

from math_game_bot.bot import MathGameBot

load_dotenv()
TOKEN = os.environ.get("MATH_BOT_TOKEN")


def run_bot():
    """Start the bot."""

    bot = MathGameBot(TOKEN)
    bot.run_bot()


if __name__ == "__main__":
    run_bot()
