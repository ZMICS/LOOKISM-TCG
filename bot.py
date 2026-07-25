import discord
from database import player_exists
from onboarding import create_onboarding
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix=["!", "lk ", "LK ", "Lk "],
    intents=intents
)
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")
@bot.tree.command(
    name="ping",
    description="Check if the bot is online!"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Kya bey chomu!")
@bot.tree.command(
    name="start",
    description="Begin your Journey"
)
async def start(interaction: discord.Interaction):
    if player_exists(interaction.user.id):
        await interaction.response.send_message(
            "You have already begun your journey, my child.",
            ephemeral=True
        )
        return
    embed, view = create_onboarding()
    await interaction.response.send_message(
        embed=embed,
        view=view,
        ephemeral=True
    )
@bot.command(name="start")
async def prefix_start(ctx: commands.Context):
    if player_exists(ctx.author.id):
        await ctx.send(
            "You have already begun your journey, my child."
        )
        return
    embed, view = create_onboarding()
    await ctx.send(
        embed=embed,
        view=view
    )
bot.run(Token)
