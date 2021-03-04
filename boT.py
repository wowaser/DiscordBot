import discord
import random
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import re

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("vsem preved")

@bot.event
async def on_typing(TextChannel, Member, now):
    if Member.id == 339384096524468224:
        return
    await TextChannel.send("Не пиши сюда, быдло")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "xd" in message.content.lower():
        await message.channel.send("No 'xd' allowed on this server..."
                                   " eblan suka")
    await bot.process_commands(message)
"""

THIS IS IS CUSTOM FUNCTION TO PULL SOME OF THE IMAGES I SENT TO THE CHAT

@bot.command()
async def comm(context):
    counter = 0
    async for msg in context.channel.history(limit=2000):
        if msg.author.name == "WOWASER":
            counter+=1
            name = "z"+str(counter)+".tif"
            for att in msg.attachments:
                #file.write(att + "\n")
                await att.save(name)
    await context.channel.send(counter)

#https://media.discordapp.net/attachments/449257167145533443/72
# 5141186142273586/unknown.png
"""

@bot.command()
async def anekdot(context):
    url = 'https://anekdot-z.ru/random-anekdot'
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    body = soup.find_all("p")
    shutka = body[1:]
    del shutka[-1]
    fin = str(shutka[0])

    chars_to_remove = "<p>san/br=dilt"
    for char in chars_to_remove:
        fin = fin.replace(char, "")

    await context.send(f"{fin}")

@bot.command()
async def meme(context):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) ' \
'AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15'
    }

    url = 'https://dota2.ru/memes/random/'
    res = requests.get(url, headers=headers)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    images = soup.find_all('img', {'src': re.compile('.jpg')})
    for link in soup.find_all('a'):
        print(link.get('href'))
    mem = ""
    for im in images:
        if "memes" in im['src']:
            mem = im['src']
            break
        await context.send(im['src'])
    mem = "https://dota2.ru" + mem
    await context.send(f"{mem}")



@bot.command(aliases=["random"])
async def dota_2(context):
    heroes = ['Alchemist', 'Ancient Apparition', 'Anti-Mage', 'Arc Warden',
              'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker',
              'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother',
              'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz',
              'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dark Willow',
              'Dazzle', 'Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight',
              'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan',
              'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void',
              'Grimstroke', 'Gyrocopter', 'Huskar', 'Invoker', 'Io', 'Jakiro',
              'Juggernaut', 'Keeper of the Light', 'Kunkka',
              'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina',
              'Lion', 'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Mars',
              'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling',
              'Naga Siren', "Nature's Prophet", 'Necrophos', 'Night Stalker',
              'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle',
              'Outworld Devourer', 'Pangolier', 'Phantom Assassin',
              'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna',
              'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King',
              'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer',
              'Skywrath Mage', 'Slardar', 'Slark', 'Snapfire', 'Sniper',
              'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies',
              'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw',
              'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk',
              'Underlord', 'Undying', 'Ursa', 'Vengeful Spirit', 'Venomancer',
              'Viper', 'Visage', 'Void Spirit', 'Warlock', 'Weaver',
              'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Wraith King']
    phrases = ["You should pick ", "I suggest "]
    await context.send(f"{random.choice(phrases)}{random.choice(heroes)}")

bot.run("YOUR TOKEN")