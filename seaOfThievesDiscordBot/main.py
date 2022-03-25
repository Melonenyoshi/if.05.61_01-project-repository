# bot.py
import os
from bs4 import BeautifulSoup
import requests
import discord
from discord import Intents, Client
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=".")  # Client(intents=Intents.default())
slash = SlashCommand(client)


@client.event
async def on_ready():
    activity = discord.Game(name="Sea of Thieves", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'{client.user} has connected to Discord!')


@slash.slash(name="Ping", description="Returns the delay of the bot")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
async def random(ctx):
    await ctx.send(get_description(get_soup_object("https://seaofthieves.fandom.com/wiki/Special:Random")))


@slash.slash(name="Random", description="Gets a random wiki article")
async def random(ctx):
    await ctx.send(get_description(get_soup_object("https://seaofthieves.fandom.com/wiki/Special:Random")))


@slash.slash(name="Query", description="Queries the wiki for the given search term")
async def query(ctx, search_term):
    url = "https://seaofthieves.fandom.com/wiki/Special:Search?query=" + search_term
    soup = get_soup_object(url)
    embed = discord.Embed(title=get_title(soup), description=get_description(soup), url=url)
    embed.set_thumbnail(url=get_thumbnail(soup))
    embed.set_footer(text="This instance is run by " + os.getenv('AUTHOR'))
    await ctx.send(embed=embed)


def get_soup_object(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


def get_description(soup):
    return soup.find("div", {"class": "mw-parser-output"}).findChildren("p")[0].text


def get_title(soup):
    return soup.head.title.text[:-26]


def get_thumbnail(soup):
    return soup.find("div", {"class": "mw-parser-output"}).findChildren("img")[0]['src']


client.run(TOKEN)
