import discord.utils
from discord.ext import commands
import os
import random

token = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Good morning, in the morning!")

@bot.command()
async def cookie(ctx):
    msg = ctx.message
    await msg.add_reaction("🍪")

@bot.command()
async def fact(ctx):
    facts = [
        "1 byte is 8 bits",
        "Python released February 20, 1991",
        "There are over 700 programming languages",
        "The first computer bug was an actual moth found in a computer in 1947.",
        "The first programming language was created in the 1800s by Ada Lovelace, making her the world’s first programmer.",


    ]
    my_fact = random.choice(facts)
    await ctx.send(my_fact)


@bot.command()
async def about(ctx):
    await ctx.send("I'm Elchin Bot created by E5 on 14.05.2025")



bot.run(f"{token}")

