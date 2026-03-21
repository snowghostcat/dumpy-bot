# 🎵 dump-bot

> Just dump music, what you like! Vibe coded with Claude 🤖

A simple Discord music bot powered by `yt-dlp` and `discord.py`. No Java, no Lavalink, no nonsense.

## Features

- `!play <song name or URL>` — Search and play from YouTube
- `!skip` — Skip the current song
- `!queue` — Show the current queue
- `!stop` — Stop and disconnect from voice channel

## Requirements

- Python 3.10+
- FFmpeg
- yt-dlp (latest)
- Node.js (required for YouTube JS challenge solving)

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

**3. Install Node.js**

Download and install Node.js from https://nodejs.org/

Verify:
```
node --version
```

**4. Install yt-dlp**

```
pip install yt-dlp
```

**5. Install EJS (YouTube challenge solver)**

```
yt-dlp --install-remote-components ejs:github
```

**6. Clone and install dependencies**

```
git clone https://github.com/yourname/dump-bot.git
cd dump-bot
pip install -r requirements.txt
```

---

### Linux (Ubuntu / Debian)

**1. Install Python, FFmpeg, and Node.js**

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg nodejs -y
```

**2. Install yt-dlp (latest)**

```bash
pip install yt-dlp --break-system-packages
```

> ⚠️ Make sure yt-dlp is up to date. Old versions will fail with YouTube.

**3. Install EJS (YouTube challenge solver)**

```bash
yt-dlp --install-remote-components ejs:github
```

**4. Clone and install dependencies**

```bash
git clone https://github.com/snowghostcat/dump-bot.git
cd dump-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

**1. Bot Token**

Create a `.env` file in the project root:
```
DISCORD_TOKEN=your_token_here
```

**2. YouTube Cookies (required to avoid rate limiting)**

Export cookies from your browser on a machine that has YouTube logged in:

```bash
yt-dlp --cookies-from-browser chrome --cookies cookies.txt --skip-download "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Place `cookies.txt` in the project root. Refresh it periodically when rate limiting occurs again.

> ⚠️ Use a browser where you are logged into YouTube. Supported browsers: `chrome`, `firefox`, `edge`

## Running

```bash
# Linux (with venv)
source venv/bin/activate
python3 main.py

# Windows
python main.py
```

## requirements.txt

```
discord.py[voice]
yt-dlp
python-dotenv
```

## Troubleshooting

| Error | Fix |
|-------|-----|
| `RuntimeError: davey library needed` | Run `pip install "discord.py[voice]"` |
| `No supported JavaScript runtime` | Install Node.js and run `yt-dlp --install-remote-components ejs:github` |
| `rate-limited by YouTube` | Re-export `cookies.txt` from your browser |
| `This video is not available` | Video is region-blocked or removed, nothing to fix |
| `Requested format is not available` | Update yt-dlp: `pip install -U yt-dlp` |

## Notes

- The bot requires **Message Content Intent** to be enabled in the [Discord Developer Portal](https://discord.com/developers/applications)
- Make sure the bot has permissions: `Connect`, `Speak`, `Send Messages`, `Read Message History`
- Keep yt-dlp up to date: `pip install -U yt-dlp`
- Refresh `cookies.txt` if YouTube starts rate limiting again