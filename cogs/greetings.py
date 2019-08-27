import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(client):
        print(f'We are online {client}')
    # await utils.set_presence(client)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Para de pingar mardito")


def setup(client):
    client.add_cog(Greetings(client))
