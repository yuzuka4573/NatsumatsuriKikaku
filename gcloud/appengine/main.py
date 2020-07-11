import os

import discord
from discord.ext import commands
import googleapiclient.discovery

# GCP
compute = googleapiclient.discovery.build('compute', 'v1')
project = os.getenv('GOOGLE_CLOUD_PROJECT')
zone = 'us-central1-a'
instance = 'instance-1'

# Bot
description = """サーバを操作するためのBotだよ！"""
bot = commands.Bot(command_prefix='?', description=description)

@bot.command(name='status')
async def _get(ctx):
    """✅ サーバの状態を確認する"""
    result = compute.instances() \
        .get(project=project, zone=zone, instance=instance) \
        .execute()
    status = result['status']
    await ctx.send(f'✅ サーバの状態: {status}')

@bot.command()
async def start(ctx):
    """⏰ サーバを起動する"""
    compute.instances() \
        .start(project=project, zone=zone, instance=instance) \
        .execute()
    await ctx.send('⏰ サーバの起動を受け付けたよ！ちょっと待ってね...')

@bot.command()
async def stop(ctx):
    """💤 サーバを停止する"""
    compute.instances() \
        .stop(project=project, zone=zone, instance=instance) \
        .execute()
    await ctx.send('💤 サーバの停止を受け付けたよ！ちょっと待ってね...')

bot.run(os.environ['DISCORD_BOT_TOKEN'])
