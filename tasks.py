
import dynmap
import discord 

from discord.ext import commands
from discord import app_commands
import setup as s 

import cmds.get, cogs.tasks, cmds.poll

import os

bot = commands.Bot(s.default_prefix, intents=discord.Intents.default())
client = dynmap.Client(bot, "https://map.rulercraft.com")

tree : app_commands.CommandTree = bot.tree
bot.client = client 

@bot.event 
async def on_interaction(interaction : discord.Interaction):
    interaction.response._responded = True

@bot.event 
async def on_ready():
    cogs.tasks.get_world_task(bot, client).start()

async def setup_hook():

    await bot.load_extension("cmds.errors")

bot.setup_hook = setup_hook

bot.run(os.getenv("token"))