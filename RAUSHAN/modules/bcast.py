import asyncio
import time
from pyrogram import filters
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from config import Config
from RAUSHAN import app
from RAUSHAN.Helpers.mongo import (
    get_served_chats,
    get_served_users,
    remove_served_user,
    remove_served_chat,
)

IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID))
async def broadcast_message(client, message):
    global IS_BROADCASTING

    if IS_BROADCASTING:
        return await message.reply_text("🚫 **ʙʀᴏᴀᴅᴄᴀsᴛ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ**")

    start_time = time.time()

    flags = message.text.lower()
    do_pin = "-pin" in flags

    if message.reply_to_message:
        payload = message.reply_to_message
        use_forward = True
        y = message.chat.id
        x = payload.id  # ✅ FIXED HERE
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**» ᴜsᴀɢᴇ :**\n"
                "• /broadcast Your Message\n"
                "• ɪɴ ᴀɴʏ ᴍᴇssᴀɢᴇ ʀᴇᴘʟʏ /broadcast\n"
                "• /broadcast -pin Your Text [ғᴏʀ ᴘɪɴ]"
            )

        payload = message.text.replace("-pin", "").split(None, 1)[1].strip()
        use_forward = False

        if not payload:
            return await message.reply_text("❌ **ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ.**")

    IS_BROADCASTING = True
    sent = failed = pin = 0
    usent = ufailed = 0

    chats = await get_served_chats()
    for chat in chats:
        chat_id = int(chat["chat_id"])
        try:
            m = (
                await app.forward_messages(chat_id, y, x)
                if use_forward
                else await app.send_message(chat_id, payload)
            )

            if do_pin:
                await m.pin(disable_notification=True)
                pin += 1

            sent += 1

        except FloodWait as e:
            if e.value <= 200:
                await asyncio.sleep(e.value)
        except Exception:
            failed += 1
            await remove_served_chat(chat_id)

    users = await get_served_users()
    for user in users:
        user_id = int(user["user_id"])
        try:
            await (
                app.forward_messages(user_id, y, x)
                if use_forward
                else app.send_message(user_id, payload)
            )
            usent += 1

        except (UserIsBlocked, InputUserDeactivated):
            ufailed += 1
            await remove_served_user(user_id)
        except FloodWait as e:
            if e.value <= 200:
                await asyncio.sleep(e.value)
        except Exception:
            ufailed += 1

    IS_BROADCASTING = False

    time_taken = int(time.time() - start_time)

    await message.reply_text(
        f"✅ **ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ**\n\n"
        f"🏘 **ᴄʜᴀᴛs :-** `{sent}`\n"
        f"📌 **ᴘɪɴs :-** `{pin}`\n"
        f"👤 **ᴜsᴇʀs :-** `{usent}`\n"
        f"❌ **ғᴀɪʟᴇᴅ :-** `{failed + ufailed}`\n\n"
        f"⏱ **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ :-** `{time_taken} ꜱᴇᴄ`"
    )
