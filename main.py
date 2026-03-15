import asyncio
import discord
from discord.ext import commands
import yt_dlp

# yt-dlp options
YDL_OPTS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0',
    'cookiesfrombrowser': ('firefox')
}

FFMPEG_OPTS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# queue stored per guild
queues: dict[int, list] = {}


def get_queue(guild_id: int) -> list:
    if guild_id not in queues:
        queues[guild_id] = []
    return queues[guild_id]


def search_yt(query: str) -> dict | None:
    with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
        try:
            info = ydl.extract_info(query, download=False)
            if 'entries' in info:
                info = info['entries'][0]
            return info
        except Exception:
            return None


async def play_next(ctx: commands.Context):
    queue = get_queue(ctx.guild.id)
    if not queue:
        return

    info = queue.pop(0)
    url = info['url']
    title = info.get('title', 'Unknown')

    source = discord.FFmpegPCMAudio(url, **FFMPEG_OPTS)
    ctx.voice_client.play(
        source,
        after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop)
    )
    await ctx.send(f'🎵 Now playing: **{title}**')


@bot.command()
async def play(ctx: commands.Context, *, query: str):
    # check if user is in a voice channel
    if not ctx.author.voice:
        return await ctx.send('❌ Please join a voice channel first.')

    # join or move to user's voice channel
    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()
    elif ctx.voice_client.channel != ctx.author.voice.channel:
        await ctx.voice_client.move_to(ctx.author.voice.channel)

    await ctx.send(f'🔍 Searching for: **{query}**')

    # run search in executor to avoid blocking the event loop
    info = await asyncio.get_event_loop().run_in_executor(None, search_yt, query)
    if not info:
        return await ctx.send('❌ No results found.')

    queue = get_queue(ctx.guild.id)
    queue.append(info)

    if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
        await ctx.send(f'➕ Added to queue: **{info.get("title")}**')
    else:
        await play_next(ctx)


@bot.command()
async def skip(ctx: commands.Context):
    if not ctx.voice_client or not ctx.voice_client.is_playing():
        return await ctx.send('❌ Nothing is playing right now.')
    ctx.voice_client.stop()  # after callback will trigger play_next
    await ctx.send('⏭️ Skipped.')


@bot.command()
async def queue(ctx: commands.Context):
    q = get_queue(ctx.guild.id)
    if not q:
        return await ctx.send('📭 The queue is empty.')
    lines = [f'{i+1}. {info.get("title", "Unknown")}' for i, info in enumerate(q)]
    await ctx.send('📋 Queue:\n' + '\n'.join(lines))


@bot.command()
async def stop(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send('❌ Bot is not in a voice channel.')
    queues.pop(ctx.guild.id, None)
    await ctx.voice_client.disconnect()
    await ctx.send('👋 Disconnected.')


bot.run('TOKEN')