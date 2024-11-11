from app.models import User
from werkzeug.security import generate_password_hash

# Create a new user
def create_user(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        email=data['email'],
        password=hashed_password,
        name=data['name']
    )
    new_user.save()
    return new_user

# Get a user by email
def get_user_by_email(email):
    return User.objects(email=email).first()

# Update an existing user
def update_user(email, data):
    user = User.objects(email=email).first()
    if not user:
        return None

    if 'name' in data:
        user.name = data['name']
    
    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='sha256')

    user.save()
    return user

# Delete a user
def delete_user(email):
    user = User.objects(email=email).first()
    if user:
        user.delete()
        return True
    return False
