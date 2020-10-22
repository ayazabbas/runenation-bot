# bot.py
import config
import os
import random
import sheetreader
import logging

from discord.ext import commands


bot = commands.Bot(command_prefix="!rn ")
logger = logging.getLogger()


@bot.event
async def on_ready():
    logger.info(f"{bot.user} is connected to guilds {bot.guilds}")


@bot.command(name="tob")
async def tob(ctx, *, rsn):
    logger.info(f"Command: f{ctx.message}")
    response = sheetreader.tob(rsn, "TOB")
    logger.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.command(name="cox")
async def cox(ctx, *, rsn):
    logger.info(f"Command: f{ctx.message}")
    response = sheetreader.cox(rsn, "COX")
    logger.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.command(name="cm")
async def cm(ctx, *, rsn):
    logger.info(f"Command: f{ctx.message}")
    response = sheetreader.cox(rsn, "COX CM")
    logger.info(f"Sending response: {response}")
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    logger.error(error)
    await ctx.send(f"Zamorak has misguided us. {error}")


bot.run(config.TOKEN)
