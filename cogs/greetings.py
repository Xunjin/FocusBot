import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'[MEMBER JOINED] - {member}')

def setup(client):
    client.add_cog(Greetings(client))
