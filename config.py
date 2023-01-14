
from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "19099900"))
API_HASH = getenv("API_HASH", "2b445de78e5baf012a0793e60bd4fbf5")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5793939143:AAFF3tL5x6CaZmzQbLojtPU6B9kpVjPR4pg")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "5402276336").split())
)  # Input type must be interger
