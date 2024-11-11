from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URL"))
db = client['internshala']
user_collection = db['users']

# Function to create a user
def create_user(email, username, password):
    hashed_password = generate_password_hash(password)
    user_collection.insert_one({"email": email, "username": username, "hashed_password": hashed_password})
    print(f"User {username} created.")

# Function to update a user's password
def update_user(email, new_password):
    hashed_password = generate_password_hash(new_password)
    result = user_collection.update_one(
        {"email": email},
        {"$set": {"hashed_password": hashed_password}}
    )
    if result.modified_count > 0:
        print(f"Password for {email} updated successfully.")
    else:
        print(f"No user found with email {email}.")

# Function to get a user's details
def get_user(email):
    user = user_collection.find_one({"email": email})
    if user:
        print(f"User Details - Email: {user['email']}, Username: {user['username']}")
    else:
        print(f"No user found with email {email}.")

# Function to delete a user
def delete_user(email):
    result = user_collection.delete_one({"email": email})
    if result.deleted_count > 0:
        print(f"User with email {email} deleted.")
    else:
        print(f"No user found with email {email}.")

if __name__ == "__main__":
    # Create user
    create_user("admin@example.com", "admin", "adminpassword")

    # Get user
    get_user("admin@example.com")

    # Update user
    update_user("admin@example.com", "newadminpassword")

    # Get updated user
    get_user("admin@example.com")

    # Delete user
    delete_user("admin@example.com")
