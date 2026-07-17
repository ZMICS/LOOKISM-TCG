import discord
from database import player_exists, create_player
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
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
async def start(interaction:discord.Interaction):
    if player_exists(interaction.user.id):
        await interaction.response.send_message(
            "You have already begun your journey my child",
            ephemeral=True
        )
        return
    embed=discord.Embed(
        title="WELCOME TO LOOKISM TCG BOT",
        description=(
            "Your journey into the lookism world is about to begin.\n\n"
            "Do you want to proceed?"
        )
    )
    view=discord.ui.View()
    begin_button=discord.ui.Button(
        label="Begin Journey",
        style=discord.ButtonStyle.success
    )
    view.add_item(begin_button)
    async def begin_callback(button_interaction: discord.Interaction):
        create_player(
            button_interaction.user.id,
            button_interaction.user.name
        )
        await button_interaction.response.send_message(
            "Welcome You have recieved 250 tokens",
            ephemeral=True
        )
        begin_button.callback = begin_callback
    await interaction.response.send_message(
        embed=embed,
        view=view
    )    
bot.run(Token)

