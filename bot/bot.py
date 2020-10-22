# bot.py
import config
import os
import random
import sheetreader

from discord.ext import commands


bot = commands.Bot(command_prefix="!rn ")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected")


@bot.command(name="tob")
async def tob(ctx, *, rsn):
    response = sheetreader.tob(rsn, "TOB")
    await ctx.send(response)


@bot.command(name="cox")
async def tob(ctx, *, rsn):
    response = sheetreader.cox(rsn, "COX")
    await ctx.send(response)


@bot.command(name="cm")
async def tob(ctx, *, rsn):
    response = sheetreader.cox(rsn, "COX CM")
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    print(f"ERROR: {error}")
    await ctx.send(f"Zamorak has misguided us. {error}")


bot.run(config.TOKEN)
