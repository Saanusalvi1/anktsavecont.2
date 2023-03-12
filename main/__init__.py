

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23980112
API_HASH = "2a7c2cc34b071aa6f9877baf0c43ca3f"
BOT_TOKEN = "6262783032:AAEKExDzesttyI-naespk6iA7eD9UPmvUBc"
SESSION = "BQBrtpm4Pw5O6Cqx14J-mXBpgpsW9zPr81tY9qCdlkyKgU8ExHOJCa3gvEcdTwN86lEvZhSv1ouXIu9L2_kNcu4Bmqa-2KPAYffc2PVadclA0QSM4aDkV9wrgPeGJkVsd9ChicxQvKtIxS_6QiO_-mcu67zH4pp2QghY8qJ2p22kRsklNAdx0x60gRdLcr7TcotrxZ2u1l9xYFqk8ibFlh3rH3oYru86mJu_dmldfOHAPkzjUf3FGgfKWKIqIr92afFKB3svQZTvNm0Jhor4Hsi6hNWq7sXnTWxjxZNQoxwMjBWe1iGauNYQt049gR1hcn1yUp95kqiddObYgduVU2VhAAAAAWWAOYwA"
FORCESUB = "Shabk"
AUTH = 5997869452

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
