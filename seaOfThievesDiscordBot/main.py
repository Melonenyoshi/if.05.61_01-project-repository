# bot.py
import os
import traceback
import time
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
    if "429" in extext:
        embed = discord.Embed(title="The execution has been rate limited",
                              description="\u200b",
                              color=0xffa500)
        embed.set_footer(text="This instance is hosted by " + HOST)
        while True:
            try:
                await ctx.send(embed=embed)
                return
            except discord.errors.HTTPException:
                time.sleep(1)
    else:
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
        await Article("https://seaofthieves.fandom.com/wiki/" +
                      value.split(';')[0]).send(ctx, value.split(';')[1])


@slash.slash(name="Ping", description="Returns the delay of the bot")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@slash.slash(name="Test", description="Queries a random article the given amount of times")
async def test(ctx, times):
    times = int(times)
    while times > 0:
        await Article().send(ctx)
        times -= 1


@slash.slash(name="Random", description="Gets a random wiki article")
async def random(ctx):
    await Article().send(ctx)


@slash.slash(name="Query", description="Queries the wiki for the given search term")
async def query(ctx, search_term):
    await Article("https://seaofthieves.fandom.com/wiki/Special:Search?query=" + search_term).send(ctx)


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

    async def send(self, ctx, *section):
        if self.get_select(*section):
            await ctx.send(embed=self.get_embed(*section), components=[self.get_select(*section)])
        else:
            await ctx.send(embed=self.get_embed(*section))

    def get_embed(self, *section):
        if self.soup is not None:
            global last_url
            last_url = self.get_url()
            if section:
                text = ""
                for element in self.soup.find("span", {"id": section[0]}).parent.findNextSiblings():
                    if element.findChildren("span", {"class": "mw-headline"}) or (
                            element.has_attr('style') and "clear:both" in element['style']):
                        break
                    text += element.text
                embed = discord.Embed(title=self.soup.find("span", {"id": section[0]}).text,
                                      description=text,
                                      color=0x10938a)
            else:
                embed = discord.Embed(title=self.get_title(),
                                      description=self.get_description(),
                                      url=self.get_url(),
                                      color=0x10938a)
                if self.get_image() is not False:
                    embed.set_image(url=self.get_image())
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
                                                    value=tr.findChildren(recursive=False)[1].text,
                                                    inline=True)
        else:
            embed = discord.Embed(title="Error 404", description="Article not found", color=0xff0000)
        embed.set_footer(text="This instance is hosted by " + HOST)
        return embed

    def get_select(self, *section):
        if self.soup is None:
            return
        options = []
        if section:
            h_level = int(str(self.soup.find("span", {"id": section[0]}).parent)[2])
            for span in self.soup.find("span", {"id": section[0]}).findAllNext("span", {"class": "mw-headline"}):
                if "h" + str(int(h_level + 1)) in str(span.parent):
                    options.append(create_select_option(span.text, value=str(self.get_url() + ";" + span['id'])[37:]))
                if "h" + str(h_level) in str(span.parent):
                    break
        else:
            for span in self.soup.find("div", {"class": "mw-parser-output"}).\
                    findChildren("span", {"class": "mw-headline"}):
                if "h2" in str(span.parent):
                    options.append(create_select_option(span.text, value=str(self.get_url() + ";" + span['id'])[37:]))
        if len(options) < 1:
            return
        select = create_select(
            options=options,
            placeholder="Further information",
            max_values=len(options)
        )
        return create_actionrow(select)

    def get_title(self):
        return self.soup.head.title.text[:-26]

    def get_description(self):
        if self.soup.find("div", {"class": "mw-parser-output"}).findChildren("p", recursive=False):
            return self.soup.find("div", {"class": "mw-parser-output"}).findChildren("p", recursive=False)[0].text
        return "\u200b"

    def get_url(self):
        return self.soup.find('meta', attrs={"name": "twitter:url"})['content']

    def get_image(self):
        try:
            if self.soup.find("table", {"class": "infoboxtable"}):
                for a in self.soup.find("table", {"class": "infoboxtable"}).findChildren("a"):
                    if a.findChildren("img") and "http" in a["href"]:
                        return a["href"]
        except IndexError:
            pass
        return False


client.run(TOKEN)
