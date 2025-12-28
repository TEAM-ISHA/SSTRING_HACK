from pyrogram import filters
from pyrogram.types import CallbackQuery
from pyrogram.errors import UserIsBlocked, InputUserDeactivated

from config import LOGGER_GROUP_ID
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
)


@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user = message.from_user
    user_id = user.id
    username = f"@{user.username}" if user.username else "N/A"
    mention = user.mention
    bot = (await client.get_me()).mention

    try:
    
        await add_served_user(user_id)

        await message.reply_photo(
            photo=START_PIC,
            caption=PM_TEXT.format(mention, bot),
            reply_markup=PM_BUTTON,
        )

    except (UserIsBlocked, InputUserDeactivated):
        await remove_served_user(user_id)
        return
    except Exception:
        return

    log_msg = (
        "**✦ ηєᴡ ᴜsєʀ sᴛᴧʀᴛєᴅ ᴛʜє ʙσᴛ**\n\n"
        f"**➻ ᴜsєʀ :** [{user.first_name}](tg://user?id={user_id})\n"
        f"**➻ ᴜsєʀɴᴀᴍᴇ :** {username}\n"
        f"**➻ ɪᴅ :** `{user_id}`"
    )

    try:
        await client.send_message(LOGGER_GROUP_ID, log_msg)
    except:
        pass


@app.on_message(filters.command("hack") & filters.private)
async def hack_cmd(client, message):
    try:
        await message.reply_text(
            HACK_TEXT,
            reply_markup=HACK_MODS,
        )
    except (UserIsBlocked, InputUserDeactivated):
        await remove_served_user(message.from_user.id)
    except Exception:
        pass


@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(client, query: CallbackQuery):
    await query.message.edit_text(
        HACK_TEXT,
        reply_markup=ALPHA_MODS
    )
    await query.answer()


@app.on_callback_query(filters.regex("back_btn"))
async def back_callback(client, query: CallbackQuery):
    await query.message.edit_text(
        PM_TEXT,
        reply_markup=PM_BUTTON
    )
    await query.answer()
    
