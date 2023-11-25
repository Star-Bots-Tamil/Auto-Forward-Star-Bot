import logging
import json
from os import getenv, path

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

load_dotenv(".env")

logging.basicConfig(
    format="[ %(asctime)s: %(levelname)-8s ] %(name)-20s - %(message)s",
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING)

# load json file
config_name = "channel_list.json"
if not path.isfile(config_name):
    LOGGER.error("No channel_list.json config file found! Exiting...")
    exit(1)
with open(config_name, "r") as data:
    CONFIG = json.load(data)


API_KEY = getenv("API_KEY", "6460834619:AAHyB5jkF2QXpSaCW620YmbdvFVztfcHwSM")
if not API_KEY:
    LOGGER.error("No API_KEY token provided!")
    exit(1)
OWNER_ID = int(getenv("OWNER_ID", "1391556668"))
REMOVE_TAG = getenv("REMOVE_TAG", "True") in {"true", "True", 1}

bot = ApplicationBuilder().token(BOT_TOKEN).build()
