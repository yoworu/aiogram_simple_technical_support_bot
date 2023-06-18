from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
MAIN_CHAT_ID = getenv('MAIN_CHAT_ID')
