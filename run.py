"""Execute the bot."""

import os

from math_game_bot.bot import MathGameBot

if __name__ == "__main__":
    TOKEN = os.environ.get("MATH_BOT_TOKEN")
    bot = MathGameBot(TOKEN)
    bot.run_bot()
