import discord
from discord.ext import commands


class MemberJoin(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'[MEMBER JOINED] - {member}')

def setup(client):
    client.add_cog(MemberJoin(client))
