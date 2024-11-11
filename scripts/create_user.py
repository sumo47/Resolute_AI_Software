from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URL"))
db = client['internshala']
user_collection = db['users']

def create_user(email, username, password):
    hashed_password = generate_password_hash(password)
    user_collection.insert_one({"email": email, "username": username, "hashed_password": hashed_password})

if __name__ == "__main__":
    create_user("admin@example.com", "admin", "adminpassword")
    print("Admin user created")
