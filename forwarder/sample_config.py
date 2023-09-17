import os

if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    REMOVE_TAG = True

    # REQUIRED
    API_KEY = "617722711:AAHysCHsVcQja6LOlHa88101lKjrxez80-M"  # API key obtained from BotFather
    OWNER_ID = "1391556668"  # If you dont know, run the bot and do /id in your private chat with the bot

    FILES_FILTERS = "video document"
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", FILES_FILTERS).split()))
    
    # FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS = [-1001822541447]  # List of chat id's to forward messages from
    TO_CHATS = [-1001871766752]  # List of chat id's to forward messages to

    # Channel 1 FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS_1 = [-1001234704297]  # List of chat id's to forward messages from
    TO_CHATS_1 = [-1001128355490]  # List of chat id's to forward messages to

    # Channel 2 FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS_2 = [-1001234704297]  # List of chat id's to forward messages from
    TO_CHATS_2 = [-1001128355490]  # List of chat id's to forward messages to

    # Channel 3 FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS_3 = [-1001234704297]  # List of chat id's to forward messages from
    TO_CHATS_3 = [-1001128355490]  # List of chat id's to forward messages to

    # Channel 4 FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS_4 = [-1001234704297]  # List of chat id's to forward messages from
    TO_CHATS_4 = [-1001128355490]  # List of chat id's to forward messages to

    # Channel 5 FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS_5 = [-1001234704297]  # List of chat id's to forward messages from
    TO_CHATS_5 = [-1001128355490]  # List of chat id's to forward messages to


    # FOR WEBHOOKS
    WEBHOOK = False
    IP_ADDRESS = "127.0.0.1"  # Use "0.0.0.0" if using Heroku
    URL = None  # The URL that the bot should listen to for updates
    PORT = 5000  # Port to listen on for webhooks
    CERT_PATH = None  # Path to certificate file

    WORKERS = 4  # Depends on usage, 4 by default


class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True
