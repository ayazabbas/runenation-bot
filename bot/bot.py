# bot.py
import config
import os
import random
import sheetreader
import logging

from discord.ext import commands


bot = commands.Bot(command_prefix="!rn ")


@bot.event
async def on_ready():
    print(f"{bot.user} is connected to guilds {bot.guilds}")


@bot.command(name="tob")
async def tob(ctx, *, rsn):
    logging.info(f"Command: f{ctx.message}")
    response = sheetreader.tob(rsn, "TOB")
    logging.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.command(name="cox")
async def cox(ctx, *, rsn):
    logging.info(f"Command: f{ctx.message}")
    response = sheetreader.cox(rsn, "COX")
    logging.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.command(name="cm")
async def cm(ctx, *, rsn):
    logging.info(f"Command: f{ctx.message}")
    response = sheetreader.cox(rsn, "COX CM")
    logging.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    logging.error(error)
    await ctx.send(f"Zamorak has misguided us. {error}")


bot.run(config.TOKEN)
