from pymongo import MongoClient
from .config import config

client = MongoClient(config.DATABASE_URL)
db = client['internshala']
user_collection = db['users']
