# Math Game Bot

A discord bot for a simple math game, written using Discord.py and packaged with Poetry.

Per [PROJECTS.md](https://github.com/dacoder101/dacoder101/blob/main/PROJECTS.md),

> A Discord.py math game bot inspired by those math worksheets where students use a set of numbers, and write equations for every number, in say one through twenty. Made so I can grasp Discord bot development a little more, and just code some Python, which I haven't used to make any large projects for a while.

## Contributing/Executing

Install all dependencies using `poetry install` after cloning the repository. You will need to configure your IDE with the virtual environment it generates, or it may not detect the installed dependencies, or execute the script with `poetry run` directly.

The `MATH_BOT_TOKEN` environment variable must be set with your bot's token, which can be created and found on the [Discord Developer Portal](https://discord.com/developers/).

Thank you for contributing!

## Using the Bot

### Method 1

Add [this application](https://discord.com/api/oauth2/authorize?client_id=1204659279936880690&permissions=8&scope=bot) to your Discord server. You may not be able to add it to certain servers depending on the permissions you have.

**The application will not respond to any commands unless it is currently being executed on my hardware.**

### Method 2

Clone the repository, and follow the instructions for contributing. Execute `run.py`, and the bot should go online.
