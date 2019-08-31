import utils
import discord
from discord.ext import commands


class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(client):
        print('[BOT READY!]')


def setup(client):
    client.add_cog(Ready(client))
