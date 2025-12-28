from pyrogram import filters
from pyrogram.types import CallbackQuery, Message
from pyrogram.errors import UserIsBlocked, InputUserDeactivated

from config import Config
from RAUSHAN import app, START_PIC
from RAUSHAN.Helpers.data import (
    PM_TEXT,
    PM_BUTTON,
    HACK_TEXT,
    HACK_MODS,
    ALPHA_MODS,
)
from RAUSHAN.Helpers.mongo import (
    add_served_user,
    remove_served_user,
    add_served_chat,
    remove_served_chat,
)


@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    user = message.from_user
    bot = (await client.get_me()).mention

    try:
        await add_served_user(user.id)

        
        try:
            await message.reply_photo(
                photo=START_PIC,
                caption=PM_TEXT.format(user.mention, bot),
                reply_markup=PM_BUTTON,
            )
        except Exception as e:
        
            print("START PHOTO ERROR:", e)
            await message.reply_text(
                PM_TEXT.format(user.mention, bot),
                reply_markup=PM_BUTTON,
            )

    except (UserIsBlocked, InputUserDeactivated):
        await remove_served_user(user.id)
        return
    except Exception as e:
        print("START CMD ERROR:", e)
        return

    
    log_msg = (
        "**✦ ηєᴡ ᴜsєʀ sᴛᴀʀᴛєᴅ ᴛʜє ʙσᴛ**\n\n"
        f"**➻ ᴜsєʀ :** [{user.first_name}](tg://user?id={user.id})\n"
        f"**➻ ᴜsєʀɴᴀᴍᴇ :** @{user.username if user.username else 'N/A'}\n"
        f"**➻ ɪᴅ :** `{user.id}`"
    )

    try:
        await client.send_message(Config.LOGGER_GROUP_ID, log_msg)
    except:
        pass



@app.on_message(filters.command("hack") & filters.private)
async def hack_cmd(client, message: Message):
    try:
        await message.reply_text(
            HACK_TEXT,
            reply_markup=HACK_MODS,
        )
    except (UserIsBlocked, InputUserDeactivated):
        await remove_served_user(message.from_user.id)
    except Exception as e:
        print("HACK CMD ERROR:", e)


@app.on_callback_query(filters.regex("^hack_btn$"))
async def hack_callback(client, query: CallbackQuery):
    try:
        await query.message.edit_text(
            HACK_TEXT,
            reply_markup=ALPHA_MODS,
        )
        await query.answer()
    except Exception as e:
        print("HACK CALLBACK ERROR:", e)


@app.on_callback_query(filters.regex("^back_btn$"))
async def back_callback(client, query: CallbackQuery):
    user = query.from_user
    bot = (await client.get_me()).mention

    try:
        await query.message.edit_text(
            PM_TEXT.format(user.mention, bot),
            reply_markup=PM_BUTTON,
        )
        await query.answer()
    except Exception as e:
        print("BACK CALLBACK ERROR:", e)



@app.on_message(filters.new_chat_members)
async def on_bot_added(client, message: Message):
    bot_id = (await client.get_me()).id

    if bot_id not in [u.id for u in message.new_chat_members]:
        return

    try:
        await add_served_chat(message.chat.id)
    except Exception as e:
        print("ADD CHAT ERROR:", e)



@app.on_message(filters.left_chat_member)
async def on_bot_removed(client, message: Message):
    bot_id = (await client.get_me()).id

    if message.left_chat_member.id != bot_id:
        return

    try:
        await remove_served_chat(message.chat.id)
    except Exception as e:
        print("REMOVE CHAT ERROR:", e)
