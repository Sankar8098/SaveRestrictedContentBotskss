#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23275126
API_HASH = "532c54bbe1c3f2296981f02469455915"
BOT_TOKEN = "6245941590:AAHmjYyg9uELAU9UkfjYQN9pNh2Dq1_RgBQ"
SESSION = "BQFjJnYAN1WA2dSQfMbFHu86rCi6JCTDVD-YDkY1dMLNVDKVlO7jA3s1jFbobICYUDjsbd4wM5EPsBUe2HLBGpaHPKL74jPJjzp0bEc4hui0tidJv4Klj7hduCWIJT0l8cRSTjgihq8ZaIgdFTatmrwgD3n8xdMyqb0CU8KY2DF6i6J_XYchIEwkm9RHbBsmnXipSwCALXvsT3iBfodxOQg9pCd9_UnxDifIIy59U_7FJsiXiAsHVIxKQoPzL9fIQXyBchxQw54emgEVKl7640XHoANJNMicvFQcJhS7jjeMGB1iE4y5RnCozFXiFyileEAp3NV5a6LaqfYBySQDJA2SdfgxLwAAAAFSbLt8AA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5677824892

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
