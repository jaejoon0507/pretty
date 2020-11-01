import asyncio,discord,os
from discord.ext import commands

to = os.path.dirname( os.path.abspath( __file__ ) )+"/token.txt"
t = open(to,"r",encoding="UTF-8")
token = t.read().split()[0]

print("확인: ",to)
compile = discord.Client()

bot = commands.Bot(command_prefix='!',status=discord.Status.online)

@bot.event
async def on_ready():
    print("봇 시작")

@bot.command()
async def 녕(ctx, arg):
    if arg == "안녕":
        await ctx.send("안뇽~~")
    else:
        await ctx.send("???")


bot.run(token)