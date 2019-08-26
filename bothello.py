from os import environ

import discord
from discord.ext import commands

import utils


token_bot = environ.get('BOT')
client = discord.Client()


client.add_cog(Cog(client))


@client.event
async def on_ready():
    print(f'We have looged in as {client.user}')
    await utils.set_presence(client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'[MESSAGE]: [{message.author}] - {message.content}')

    if message.content.startswith('$hello'):
        await message.channel.send('fuck you')


client.run(token_bot)
