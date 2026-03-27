from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Aapki API Details
API_ID = int(getenv("API_ID", "21803165"))
API_HASH = getenv("API_HASH", "05e5e695feb30e25bef47484cc006da7")

# Bot Token jo aapne diya tha
BOT_TOKEN = getenv("BOT_TOKEN", "8645782241:AAHDC-tfWTqCvFSTFlKT3yMxfdUoh4tj9Hw")

# Owner aur Channel details
OWNER_ID = int(getenv("OWNER_ID", "7812646657"))
MUST_JOIN = getenv("MUST_JOIN", "botbykilwakillua")

# Database URI
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aditya0:aditya0@cluster0.9m8897t.mongodb.net/?appName=Cluster0")
