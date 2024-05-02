import discord
import discord.ext
import discord.ext.commands
from base_classes import FileWork
from bot import bot
from bot.help_command import help
from bot.player_control import player_add, player_rm
from discord.ext import commands

TOKEN_PATH: str = "secrets/token"

@bot.command()
async def ping(ctx: discord.ext.commands.Context):
    await ctx.send(f"Pong in ({round(bot.latency * 1000)}ms)")

async def main():
    await bot.start(FileWork(TOKEN_PATH).load_data())
