import discord
from discord.ext import commands
from discord import app_commands
import os
import random
from dotenv import load_dotenv
from google import genai  # ✅ use new client

# Load secrets from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Setup Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Needed for on_member_join

# Custom bot class
class ElchinBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()  # Sync slash commands globally

bot = ElchinBot()

# === Events ===
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Good morning, in the morning!")

@bot.event
async def on_member_join(member: discord.Member):
    # Welcome message
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! 🎉")
    
    # Assign role
    role = discord.utils.get(member.guild.roles, name="Member")
    if role:
        try:
            await member.add_roles(role)
            print(f"Assigned role {role.name} to {member.name}")
        except discord.Forbidden:
            print(f"Cannot assign role {role.name} to {member.name} — check permissions")
        except Exception as e:
            print(f"Error assigning role: {e}")

# === Slash commands ===
@bot.tree.command(name="cookie", description="Get a cookie!")
async def cookie(interaction: discord.Interaction):
    await interaction.response.send_message("🍪")

@bot.tree.command(name="fact", description="Get a random programming fact")
async def fact(interaction: discord.Interaction):
    facts = [
        "1 byte is 8 bits",
        "Python released February 20, 1991",
        "There are over 700 programming languages",
        "The first computer bug was an actual moth found in 1947.",
        "Ada Lovelace created the first programming algorithm in the 1800s.",
        "The Linux kernel has over 30 million lines of code.",
        "Git was created by Linus Torvalds in 2005."
    ]
    await interaction.response.send_message(random.choice(facts))

@bot.tree.command(name="about", description="Learn about Elchin Bot")
async def about(interaction: discord.Interaction):
    await interaction.response.defer()
    app = await bot.application_info()
    owner = app.owner
    await interaction.followup.send(f"I'm Elchin Bot created by {owner.mention} on 14.05.2025")

# Roast list
roasts = [
    "You're as useless as the 'g' in lasagna.",
    "If I had a dollar for every smart thing you said, I'd be broke.",
    "You bring everyone so much joy… when you leave the room.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're about as helpful as a traffic jam.",
    "You're the beta version of a broken app.",
    "You're like a fork in a soup restaurant.",
    "You're like a broken keyboard — can’t type anything smart.",
    "You're the autocorrect that turns 'homework' into 'homewreck'.",
    "You're the captcha nobody can read.",
    "You're like lag in a boss fight.",
    "You're like printer errors — always happening, never helpful.",
    "You're the unskippable ad of my life.",
    "You're as refreshing as warm soda.",
    "You're like a pop-up ad — nobody wants you here."
]

@bot.tree.command(name="roast", description="Get a random roast")
async def roast(interaction: discord.Interaction):
    roast_msg = random.choice(roasts)
    await interaction.response.send_message(roast_msg)

# === Gemini AI Integration ===
@bot.tree.command(name="ask", description="Ask Gemini AI something")
async def ask(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()  # show "thinking"
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        await interaction.followup.send(response.text[:2000])  # Discord limit
    except Exception as e:
        await interaction.followup.send(f"Error: {e}")

# Run bot
bot.run(TOKEN)

