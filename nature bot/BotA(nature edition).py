
import discord
from discord.ext import commands
from BotA_ayarlar import *
import time

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def recycle(ctx):
    with open("nature bot/recycle1.jpg", "rb") as a:
        r1=discord.File(a)
    await ctx.send("Recycling is a key component of modern waste reduction and is the third component of the "'Reduce, Reuse, and Recycle'" waste hierarchy.")
    await ctx.send(file=r1)
    time.sleep(5)
    await ctx.send("These are recyclable materials:")
    with open("nature bot/recycle2.jpg", "rb") as b:
        r2=discord.File(b)
    await ctx.send(file=r2)
    time.sleep(3)
    await ctx.send("This is the recycling loop:")
    with open("nature bot/recycle5.jpg", "rb") as e:
        r5=discord.File(e)
    await ctx.send(file=r5)
    time.sleep(3)
    await ctx.send("Try to buy food with recyclable packages like cardboard boxes:")
    with open("nature bot/recycle7.jpg", "rb") as h:
        r8=discord.File(h)
    await ctx.send(file=r8)
    time.sleep(2)
    await ctx.send("Or, there are some kinds of recyclable plastic packages too:")
    with open("nature bot/recycle8.jpg", "rb") as i:
        r9=discord.File(i)
    await ctx.send(file=r9)
    time.sleep(3)
    await ctx.send("Recycling is important because it decreases waste materials.")
    with open("nature bot/recycle6.jpg", "rb") as f:
        r6=discord.File(f)
    await ctx.send(file=r6)
@bot.command()
async def usage(ctx):
    await ctx.send("To help nature you must decrease the usage of single-use objects because they pollute nature. Try to use reusable objects. Here are some examples of single-use objects:")
    with open("nature bot/use.jpg", "rb") as g:
        r7=discord.File(g)
    await ctx.send(file=r7)
@bot.command()
async def saving(ctx):
    await ctx.send("You can start by saving water.")
    with open("nature bot/water.jpg", "rb") as j:
        r10=discord.File(j)
    await ctx.send(file=r10)
    time.sleep(2)
    await ctx.send("You can save water by not leaving your taps running while you brush your teeth, soap up etc., turning off the tap during those in-between times, using a reusable cup when brushing your teeth and cutting your showers down to two minutes.")
    with open("nature bot/water2.jpg", "rb") as k:
        r11=discord.File(k)
    await ctx.send(file=r11)
    time.sleep(5)
    await ctx.send("You can save electricity by turning off unnecessary lights when they’re not in use, switching over from incandescent bulbs to using compact fluorescent lighting and using energy-saving appliances")
    with open("nature bot/save.jpg", "rb") as l:
        r12=discord.File(l)
    time.sleep(5)
    await ctx.send("You should save fuel because it pollutes nature. You can save fuel by using public transport like buses, subways, light rails, trains etc. or you can even use your own fuel by walking, riding a bike etc.")
    with open("nature bot/fuel.jpg", "rb") as m:
        r13=discord.File(m)
    await ctx.send(file=r13)

bot.run(ayarlar["TOKEN"])