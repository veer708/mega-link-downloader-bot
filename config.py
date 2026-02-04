import os

class Config:
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN")
    APP_ID = int(os.environ.get("29232353", 0))
    API_HASH = os.environ.get("6868788228291767c90e4346eea03f36")

    Mega_email = os.environ.get("MEGA_EMAIL", "")
    Mega_password = os.environ.get("MEGA_PASSWORD", "")

    Bot_username = os.environ.get("@Megadownlodd_bot", "")
    OWNER_ID = int(os.environ.get("6650855788", 0))

    REDIS_URI = os.environ.get("REDIS_URI")
    REDIS_PASS = os.environ.get("REDIS_PASS")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"
    ADMIN_LOCATION = "./ADOWNLOADS"
