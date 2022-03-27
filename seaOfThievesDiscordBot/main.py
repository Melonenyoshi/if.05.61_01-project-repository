# bot.py
import os
import traceback

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from discord_slash import SlashCommand, ComponentContext
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
HOST = os.getenv('HOST')

client = commands.Bot(command_prefix="We only use slash commands")
slash = SlashCommand(client, sync_commands=True)

last_url = ""


@client.event
async def on_ready():
    activity = discord.Game(name="Sea of Thieves", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_slash_command_error(ctx, ex):
    extext = str(ex)
    embed = discord.Embed(title=extext.splitlines()[0],
                          description=extext[len(extext.splitlines()[0]) + 1:],
                          color=0xff0000,
                          url=last_url)
    embed.set_footer(text="This instance is hosted by " + HOST)
    await client.get_channel(956879440418308096).send(embed=embed)
    await client.get_channel(956879440418308096).send("```py\n" +
                                                      ''.join(traceback.format_tb(tb=ex.__traceback__)) +
                                                      "```")


@client.event
async def on_component(ctx: ComponentContext):
    for value in ctx.values:
        await ctx.send(embed=Article(value.split(';')[0]).get_embed(value.split(';')[1]))


@slash.slash(name="Ping", description="Returns the delay of the bot")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@slash.slash(name="Test", description="Queries a random article the given amount of times")
async def test(ctx, times):
    times = int(times)
    while times > 0:
        article = Article()
        await ctx.send(embed=article.get_embed(), components=[article.get_select()])
        times -= 1


@slash.slash(name="Random", description="Gets a random wiki article")
async def random(ctx):
    article = Article()
    await ctx.send(embed=article.get_embed(), components=[article.get_select()])


@slash.slash(name="Query", description="Queries the wiki for the given search term")
async def query(ctx, search_term):
    article = Article("https://seaofthieves.fandom.com/wiki/Special:Search?query=" + search_term)
    await ctx.send(embed=article.get_embed(), components=[article.get_select()])


class Article:
    def __init__(self, *args):
        if args:
            self.soup = BeautifulSoup(requests.get(args[0]).text, 'html.parser')
            if "Search Results" in self.soup.find("h1", {"id": "firstHeading"}).text:
                if self.soup.find("h1", {"class": "unified-search__result__header"}) is not None:
                    self.soup = BeautifulSoup(
                        requests.get(self.soup.find_all("h1", {"class": "unified-search__result__header"})[0].
                                     findChildren("a")[0]["href"]).text, 'html.parser')
                else:
                    self.soup = None
        else:
            self.soup = BeautifulSoup(requests.get("https://seaofthieves.fandom.com/wiki/Special:Random").text,
                                      'html.parser')

    def get_embed(self, *args):
        global last_url
        last_url = self.get_url()
        if args:
            text = ""
            for element in self.soup.find("span", {"id": args[0]}).parent.findNextSiblings():
                if element.findChildren("span", {"class": "mw-headline"}) or (
                        element.has_attr('style') and "clear:both" in element['style']):
                    break
                text += element.text
            embed = discord.Embed(title=self.soup.find("span", {"id": args[0]}).text, description=text, color=0x10938a)
        elif self.soup is not None:
            embed = discord.Embed(title=self.get_title(),
                                  description=self.get_description(),
                                  url=self.get_url(),
                                  color=0x10938a)
            if self.get_thumbnail() is not False:
                embed.set_thumbnail(url=self.get_thumbnail())
            has_found_beginning = False
            if self.soup.find("table", {"class": "infoboxtable"}):
                for tr in self.soup.find("table", {"class": "infoboxtable"}).findChildren("tr"):
                    if not has_found_beginning:
                        try:
                            has_found_beginning = tr.findNext()['class'] == ['infoboxdetails']
                        except KeyError:
                            pass
                    if has_found_beginning:
                        if tr.findNext().has_attr('colspan'):
                            embed.add_field(name=tr.findNext().text, value="\u200b", inline=False)
                        else:
                            if "Cost" in tr.findNext().text and tr.findChildren('img'):
                                embed.add_field(name=tr.findNext().text,
                                                value=tr.findNext().findNext().text.strip() +
                                                      " " +
                                                      tr.findChildren('a')[0]['title'],
                                                inline=True)
                            else:
                                embed.add_field(name=tr.findNext().text,
                                                value=tr.findNext().findNext().text,
                                                inline=True)
        else:
            embed = discord.Embed(title="Error 404", description="Article not found", color=0xff0000)
        embed.set_footer(text="This instance is hosted by " + HOST)
        return embed

    def get_select(self):
        options = []
        for span in self.soup.find("div", {"class": "mw-parser-output"}).findChildren("span", {"class": "mw-headline"}):
            options.append(create_select_option(span.text, value=self.get_url() + ";" + span['id']))
        select = create_select(
            options=options,
            placeholder="Further information",
            max_values=len(options)
        )
        return create_actionrow(select)

    def get_title(self):
        return self.soup.head.title.text[:-26]

    def get_description(self):
        return self.soup.find("div", {"class": "mw-parser-output"}).findChildren("p", recursive=False)[0].text

    def get_url(self):
        return self.soup.find('meta', attrs={"name": "twitter:url"})['content']

    def get_thumbnail(self):
        try:
            return self.soup.find("table", {"class": "infoboxtable"}).findChildren("a")[0]['href']
        except IndexError:
            return False


client.run(TOKEN)
