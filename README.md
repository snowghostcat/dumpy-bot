# 🎵 dump-bot

> A dumb bot that somehow plays music. Vibe coded with Claude 🤖

A simple Discord music bot powered by `yt-dlp` and `discord.py`. No Java, no Lavalink, no nonsense.

## Features

- `!play <song name or URL>` — Search and play from YouTube
- `!skip` — Skip the current song
- `!queue` — Show the current queue
- `!stop` — Stop and disconnect from voice channel

---

## Requirements

- Python 3.10+
- FFmpeg
- yt-dlp

---

## Installation

### Windows

**1. Install Python**

Download and install Python 3.10+ from https://www.python.org/downloads/

Make sure to check **"Add Python to PATH"** during installation.

**2. Install FFmpeg**

Download FFmpeg from https://ffmpeg.org/download.html (get the Windows build)

Extract it and add the `bin` folder to your system PATH:
- Search "Environment Variables" in Start Menu
- Under "System Variables" → `Path` → Add the path to FFmpeg's `bin` folder (e.g. `C:\ffmpeg\bin`)

Verify:
```
ffmpeg -version
```

**3. Install yt-dlp**

```
pip install yt-dlp
```

**4. Clone and install dependencies**

```
git clone https://github.com/yourname/dump-bot.git
cd dump-bot
pip install -r requirements.txt
```

---

### Linux (Ubuntu / Debian)

**1. Install Python, FFmpeg, and yt-dlp**

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg -y
pip install yt-dlp --break-system-packages
```

**2. Clone and install dependencies**

```bash
git clone https://github.com/yourname/dump-bot.git
cd dump-bot
pip install -r requirements.txt
```

---

## Configuration

Open `main.py` and replace `TOKEN` at the bottom with your Discord bot token:

```python
bot.run('YOUR_TOKEN_HERE')
```

Or use a `.env` file (recommended):

1. Create a `.env` file in the project root:
```
DISCORD_TOKEN=your_token_here
```

2. Install `python-dotenv`:
```
pip install python-dotenv
```

3. Update `main.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))
```

---

## Running

```bash
python main.py        # Linux
python3 main.py       # Linux (if python3 is required)
python main.py        # Windows
```

---

## requirements.txt

```
discord.py[voice]
yt-dlp
python-dotenv
```

---

## Notes

- The bot requires **Message Content Intent** to be enabled in the [Discord Developer Portal](https://discord.com/developers/applications)
- Make sure the bot has permissions: `Connect`, `Speak`, `Send Messages`, `Read Message History`
- yt-dlp should be kept up to date to avoid YouTube playback issues: `pip install -U yt-dlp`