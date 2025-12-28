# TEAM PURVI ALL COPYRIGHT ©️
import os

class Config:
    API_ID = int(os.getenv("API_ID", "27079591"))
    API_HASH = os.getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9")
    TOKEN = os.getenv("TOKEN", None)
    MONGO_URL = os.getenv("MONGO_URL", None)
    OWNER_ID = int(os.getenv("OWNER_ID", "7473021518"))
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1003055975764"))
    START_PIC = os.getenv("START_PIC", "https://files.catbox.moe/ppvvg0.jpg")
