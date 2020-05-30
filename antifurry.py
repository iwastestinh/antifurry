import discord
from discord.ext import commands

client = discord.Client
client.remove_command('help')

@client.event
async def on_message(message):
  if "furry" in message:
    await message.delete()
    
  elif "Im a furry" in message:
    await member.ban()
    
#Made by Iwtesting with love
client.run('Token')
