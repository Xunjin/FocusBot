import discord

# Set Bot Presence
async def set_presence(client, game="Python"):
    game = discord.Game(game)
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(f'Bot precense has been set to [{game}]')
