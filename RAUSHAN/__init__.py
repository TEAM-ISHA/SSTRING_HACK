import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from RAUSHAN.Helpers.data import LOG_TEXT
from pyromod import listen 

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://files.catbox.moe/7crm69.jpg"

LOG = Console()


logging.basicConfig(level=logging.INFO)

app = Client(
    "alphababy",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def RAUSHAN():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- @Isha_bots ✅")
    LOG.print("[bold yellow]❖ ʏᴏᴜʀ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ....🤞 ɪғ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɢɪᴠᴇ ᴍᴇ ᴄʀᴇᴅɪᴛ sᴏ ʏᴏᴜ ᴀʀᴇ ʙɪɢɢᴇsᴛ ᴍᴏᴛʜᴇʀ ғ*ᴄᴋᴇʀ.🥵")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(RAUSHAN())    
