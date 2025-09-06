import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class ElchinBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
#        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()  # Sync commands globally

bot = ElchinBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Good morning, in the morning!")

# 🍪 /cookie command
@bot.tree.command(name="cookie", description="Get a cookie!")
async def cookie(interaction: discord.Interaction):
    await interaction.response.send_message("🍪")

# 📘 /fact command
@bot.tree.command(name="fact", description="Get a random programming fact")
async def fact(interaction: discord.Interaction):
    facts = [
        "1 byte is 8 bits",
        "Python released February 20, 1991",
        "There are over 700 programming languages",
        "The first computer bug was an actual moth found in a computer in 1947.",
        "Ada Lovelace created the first programming language in the 1800s.",
	"The Linux kernel has over 30 million lines of code.",
	"Git, the version control system, was created by Linus Torvalds in 2005."
    ]
    await interaction.response.send_message(random.choice(facts))

# ℹ️ /about command
@bot.tree.command(name="about", description="Learn about Elchin Bot")
async def about(interaction: discord.Interaction):
	await interaction.response.defer()
	app = await bot.application_info()
	owner = app.owner
	await interaction.followup.send(f"I'm Elchin Bot created by {owner.mention} on 14.05.2025")

# 🔥 /roast command
roasts = [
    "You're as useless as the 'g' in lasagna.",
    "If I had a dollar for every smart thing you said, I'd be broke.",
    "You bring everyone so much joy… when you leave the room.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You have something on your chin… no, the third one down.",
    "You're about as helpful as a traffic jam.",
    "You're the beta version of a broken app.",
    "You're like a fork in a soup restaurant.",
    "You're like a broken keyboard — can’t type anything smart.",
    "You're the kind of person who brings a spoon to a knife fight.",
    "You're more extra than an unpaid intern.",
    "You're as relevant as MySpace.",
    "You're a low-resolution version of a decent idea.",
    "You're like a banana in a toolbox — weird and unhelpful.",
    "You're like a tab with 47 open sites and no purpose.",
    "You're a search result that didn't help.",
    "You're a software update at 2 AM — inconvenient.",
    "You're the captcha nobody can read.",
    "You're as helpful as a flat tire on a freeway.",
    "You're a demo version of someone better.",
    "You're the ad you skip after 5 seconds.",
    "You're the autocorrect that turns 'homework' into 'homewreck'.",
    "You're the unskippable ad of my life.",
    "You're a background character in your own story.",
    "You're as refreshing as warm soda.",
    "You're the spam folder of friendship.",
    "You're like a pop-up ad — nobody wants you here.",
    "You're like lag in a boss fight.",
    "You're like printer errors — always happening, never helpful.",
    "You're like a knock-knock joke with no punchline.",
    "You're like a GPS that always says 'Recalculating.'",
    "You're like a clickbait title — full of disappointment.",
    "You're the 'before' picture in a tech upgrade.",
    "You're a cold pizza that no one ordered.",

]

@bot.tree.command(name="roast", description="Get a random roast")
async def roast(interaction: discord.Interaction):
    roast_msg = random.choice(roasts)
    await interaction.response.send_message(roast_msg)

bot.run(TOKEN)
