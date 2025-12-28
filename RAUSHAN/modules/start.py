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

import logging
import traceback

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

LOGGER = logging.getLogger("RAUSHAN-BOT")


async def tg_log(client, text: str, level="INFO"):
    try:
        await client.send_message(
            Config.LOGGER_GROUP_ID,
            f"**[{level}]**\n{text}"
        )
    except Exception as e:
        LOGGER.error(f"TG LOGGER FAILED: {e}")
        traceback.print_exc()


@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    LOGGER.info("START command triggered")

    user = message.from_user
    bot = (await client.get_me()).mention

    try:
        await add_served_user(user.id)
        LOGGER.info(f"User added to DB: {user.id}")

        try:
            await message.reply_photo(
                photo=START_PIC,
                caption=PM_TEXT.format(user.mention, bot),
                reply_markup=PM_BUTTON,
            )
            LOGGER.info("Start photo sent")

        except Exception as img_err:
            LOGGER.warning(f"Photo failed: {img_err}")
            await message.reply_text(
                PM_TEXT.format(user.mention, bot),
                reply_markup=PM_BUTTON,
            )

        await tg_log(
            client,
            f"✅ **START SUCCESS**\n"
            f"👤 User: {user.mention}\n"
            f"🆔 ID: `{user.id}`",
            level="SUCCESS"
        )

    except Exception as e:
        LOGGER.error("START CMD FAILED", exc_info=True)

        await tg_log(
            client,
            f"❌ **START ERROR**\n"
            f"👤 User ID: `{user.id}`\n"
            f"🧨 Error: `{e}`",
            level="ERROR"
        )



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
