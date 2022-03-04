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
async def add(ctx, first_numb, second_numb):
    first = 0
    second = 0
    try:
        first = int(first_numb)
        second = int(second_numb)
    except:
        await ctx.send("That aint even numbers")
    else:
        await ctx.send(f"the result is {first + second}")
@client.command()
async def web(ctx,given_search_string):
    output = ""

    #given_search_string.replace(" ", "+")

    path = "https://seaofthieves.fandom.com/wiki/Special:Search?query="+given_search_string

    request = requests.get(path)

    soup = BeautifulSoup(request.text, 'html.parser')

    output += soup.title.string

    image_div = soup.find("div", {"class": "mw-parser-output"})
    children_of_image_div = image_div.findChildren("a", {"class": "image"}, recursive=True)
    output += "\n" + children_of_image_div[0]["href"]

    first_line_div = image_div
    children_of_line_div = first_line_div.findChildren("p")

    output += "\n" + children_of_line_div[0].text

    print("output: \n"+output)

    await ctx.send(output)

client.run(TOKEN)