import os

import discord
from discord.ext import commands

description = '''サーバを操作するためのBotだよ！'''

bot = commands.Bot(command_prefix='?', description=description)

@bot.command(description='サーバの状態を確認する')
async def get(ctx):
    await ctx.send('[dry-run] サーバの状態は次の通り！')

@bot.command(description='サーバを起動する')
async def start(ctx):
    await ctx.send('[dry-run] サーバの起動を受け付けたよ！ちょっと待ってね...')

@bot.command(description='サーバを停止する')
async def stop(ctx):
    await ctx.send('[dry-run] サーバの停止を受け付けたよ！ちょっと待ってね...')

bot.run(os.environ['DISCORD_BOT_TOKEN'])
