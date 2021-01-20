import discord
client = discord.Client()

@client.event
async def on_message(message):
  if "furry" in message.content:
    await message.delete()

  if "Im a furry" in message.content:
    await message.author.ban()

client.run('Paste your token in here')
