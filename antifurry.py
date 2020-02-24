import discord
from discord.ext import commands

client = commands.Bot(command_prefix=['af!'])
client.remove_command('help')
