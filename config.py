import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29465055"))
API_HASH = getenv("API_HASH", "72d7aa07e4f70f0fbefd27347f2b2012")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6423471990:AAFlFfZD_bh9nGnI9G_NoVN4qhfht3Cw8ic")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Amala203145:Amala2031456@cluster0.t9ibfge.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002097928850"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5991943478))
BOT_NAME = getenv("BOT_NAME", "𓆩𝘼𝙬𝙖𝙧𝙞 ✘ 𝙈𝙪𝙨𝙞𝙘𓆪")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+Yc04IjINcqdhN2U1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Wife_Swapping_Indiaa_group")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION1", "BQHBmd8AlBCN8TUsl48CSVVJ9WUAOThCiP25TcLHyYJ8pV2NqOAairsWpnZjG4-FXKde3SQQMjWpBhGemzDobIOD5NEvz9VdPGKO7poK9C3PFfTKxSkQqCrS_q26U_4Wweg1xGo9vaGLUXUWbYrDPkx0aVIzmxvVIea8o3gnnF5phqIeqr35Qwzc9uccNUrLe38s5uzPOM78aYS5LGwk_fqb6lo9EFw5WReMyK-bGidF0g5AZddJnIiXKUXI97tzdK9V6cyXGmlA1QAe-ugSKqp6_cGFFHolknmateuKQIOhQk2UhPeS4IasE-ct25FHW_rttgSSc64QnDNRAPIpqfb09cMbPgAAAAGFnlu8AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = [
     "https://telegra.ph/file/96710c4f04c371f7c1b4c.jpg",
     "https://telegra.ph/file/ee1ff7cc05255e7b97aed.jpg",
     "https://telegra.ph/file/371553e03d103ec4e1596.jpg",
     "https://telegra.ph/file/d0e06eaeef72748299e2d.jpg",
     "https://telegra.ph/file/a682e7e43df897ac63966.jpg",
     "https://telegra.ph/file/5720f92d4d02eacafff13.jpg",
     "https://telegra.ph/file/7b15ab99e938b4ac1753b.jpg",
     "https://telegra.ph/file/ebf55af4b5c873d032979.jpg",
     "https://telegra.ph/file/a532cc1e0360a3c59d4f9.jpg",
     "https://telegra.ph/file/781674af4ba4ec934cc4c.jpg",
     "https://telegra.ph/file/ab1269e3fa7b821749048.jpg"
]

    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
