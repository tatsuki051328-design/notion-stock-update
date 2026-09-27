import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

def get_notion_client():
    api_key = os.getenv("NOTION_API_KEY")
    return Client(auth=api_key)