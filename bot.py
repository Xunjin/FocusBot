import utils
import discord

from os import environ
from os import listdir
from discord.ext import commands


token_bot = environ.get('BOT')

client = commands.Bot(command_prefix='!')

# Load Cog Command
@client.command()
async def load(ctx, extension):
    print(f'[LOADING EXT] - {extension}')
    client.load_extension(f'cogs.{extension}')


# Unload Cog command
@client.command()
async def unload(ctx, extension):
    print(f'[UNLOADING EXT] - {extension}')
    client.unload_extension(f'cogs.{extension}')


# Reload Cog Command
@client.command()
async def reload(ctx, extension):
    print(f'[RELOADING EXT] - {extension}')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


# Initialize Events
for filename in listdir('./cogs/events/'):
    if filename.endswith('.py'):
        print(f'[LOADING EXT] - {filename[:-3]}')
        client.load_extension(f'cogs.events.{filename[:-3]}')

# Initialize Commands
for filename in listdir('./cogs/commands/'):
    if filename.endswith('.py'):
        print(f'[LOADING EXT] - {filename[:-3]}')
        client.load_extension(f'cogs.commands.{filename[:-3]}')


client.run(token_bot)
