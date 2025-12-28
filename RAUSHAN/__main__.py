import asyncio
import importlib

from pyrogram import idle
from RAUSHAN import LOG
from RAUSHAN.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("RAUSHAN.modules." + all_module)
    LOG.print("[bold yellow]❖ ʙᴏᴛ sᴛᴀʀᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴏ ᴀɴᴅ ғ*ᴄᴋ ᴛɢ ɪᴅs 🖕")
    await idle() 
    LOG.print("[bold red]❖ ᴇʀʀᴏʀ ᴀᴀ ɢʏᴀ ᴀʙ ɢᴀɴᴅ ᴍᴀʀᴀ ʟᴇ ᴄᴏᴘʏ ᴘᴀsᴛᴇʀ 🤡 ᴀʟʟ ᴛᴀsᴋ ᴄᴀɴᴄᴇʟ 😴")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
