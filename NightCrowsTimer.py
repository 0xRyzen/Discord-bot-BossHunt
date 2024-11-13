import discord
import asyncio
from discord.ext import commands, tasks

# TOKEN = 'Your bot token here'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
# 3 hrs 25 min
@bot.command(name='spider')
async def timer1(ctx):
    await ctx.send('**Spider** has been killed!')
    await asyncio.sleep(12300)
    await ctx.send('||@everyone|| **Spider** is likely to have spawned!')

# 4 hrs 25 min
@bot.command(name='kiaron')
async def timer3(ctx):
    await ctx.send('**Kiaron** has been killed!')
    await asyncio.sleep(15900)
    await ctx.send('||@everyone|| **Kiaron** is likely to have spawned!')

# 5 hrs 25 min
@bot.command(name='grish')
async def timer2(ctx):
    await ctx.send('**Grish** has been killed!')
    await asyncio.sleep(19500)
    await ctx.send('||@everyone|| **Grish** is likely to have spawned!')

# 6 hrs 25 min
@bot.command(name='inferno')
async def timer4(ctx):
    await ctx.send('**Inferno** has been killed!')
    await asyncio.sleep(23100)
    await ctx.send('||@everyone|| **Inferno** is likely to have spawned!')

bot.run(TOKEN)
