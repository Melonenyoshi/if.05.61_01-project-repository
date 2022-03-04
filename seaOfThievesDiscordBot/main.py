# bot.py
import os
from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    activity = discord.Game(name="Sea of Thieves", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'{client.user} has connected to Discord!')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def query(ctx, search_term):
    await ctx.send(get_description(get_soup_object(search_term)))


def get_soup_object(search_term):
    return BeautifulSoup(requests.get("https://seaofthieves.fandom.com/wiki/Special:Search?query=" + search_term).text,
                         'html.parser')


def get_description(soup):
    return soup.find("div", {"class": "mw-parser-output"}).findChildren("p")[0].text


client.run(TOKEN)
