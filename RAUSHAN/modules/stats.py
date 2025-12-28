import time
from pyrogram import filters
from config import Config

from RAUSHAN import app
from RAUSHAN.Helpers.mongo import get_served_chats, get_served_users


BOT_START_TIME = time.time()
SUDOERS = filters.user(Config.SUDOERS)

def get_uptime(seconds: int):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    uptime = []
    if days:
        uptime.append(f"{days}ᴅ")
    if hours:
        uptime.append(f"{hours}ʜ")
    if minutes:
        uptime.append(f"{minutes}ᴍ")
    uptime.append(f"{seconds}ꜱ")

    return " ".join(uptime)

@app.on_message(filters.command("stats") & SUDOERS)
async def stats_command(client, message):
    start_ping = time.time()

    chats = await get_served_chats()
    users = await get_served_users()

    end_ping = time.time()
    ping_ms = round((end_ping - start_ping) * 1000, 2)

    total_chats = len(chats)
    total_users = len(users)

    uptime_seconds = int(time.time() - BOT_START_TIME)
    uptime = get_uptime(uptime_seconds)

    text = (
        f"📊 **{app.mention} ʙᴏᴛ ꜱᴛᴀᴛꜱ**\n\n"
        f"🏘 **ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ :** `{total_chats}`\n"
        f"👤 **ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ :** `{total_users}`\n"
        f"⏱ **ᴜᴘᴛɪᴍᴇ :** `{uptime}`\n"
        f"📡 **ᴘɪɴɢ :** `{ping_ms} ᴍꜱ`"
    )

    await message.reply_text(text)
