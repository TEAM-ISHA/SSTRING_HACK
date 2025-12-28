import sys
from config import Config
from motor.motor_asyncio import AsyncIOMotorClient


try:
    mongodb = AsyncIOMotorClient(Config.MONGO_URL).Alpha
except Exception as e:
    print("Please change your MongoDB URL")
    sys.exit()

chatsdb = mongodb.tgchatsdb
usersdb = mongodb.tgusersdb



async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    return bool(user)


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    if await is_served_user(user_id):
        return
    return await usersdb.insert_one({"user_id": user_id})


async def remove_served_user(user_id: int):
    return await usersdb.delete_one({"user_id": user_id})


async def get_served_chats() -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    return bool(chat)


async def add_served_chat(chat_id: int):
    if await is_served_chat(chat_id):
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    return await chatsdb.delete_one({"chat_id": chat_id})
