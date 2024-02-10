"""Command functionality for the bot."""


class MathBotCommands:
    """Command functionality for the bot."""

    def __init__(self, bot):
        @bot.command(name="ping")
        async def ping(ctx):
            """Display the ping in milliseconds."""
            latency = bot.latency * 1000
            await ctx.send(f"Ping: {latency:.2f}ms")
