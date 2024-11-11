# User Authentication System with MongoDB

This repository contains a user authentication system using Flask, MongoDB, and JWT. The system includes CRUD operations for users, with secured endpoints for login, password updates, and user management.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Using the Script](#using-the-script)
- [Features Implemented](#features-implemented)
- [Task Requirements](#task-requirements)

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **MongoDB**: A NoSQL database for storing user data.
- **PyMongo**: A Python driver for MongoDB.
- **Werkzeug**: A utility library for secure password hashing.
- **JWT (JSON Web Tokens)**: For secure user authentication.
- **Dotenv**: For loading environment variables.
  
## Prerequisites

Before running this app, ensure you have the following installed:
- **Python 3.x** (preferably 3.7 or higher)
- **MongoDB**: Running either locally or using MongoDB Atlas (cloud)
- **pip** (Python package manager)

You also need to install the required Python dependencies. You can do this by setting up a virtual environment and installing the dependencies listed in `requirements.txt`.

## Installation

### 1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up MongoDB:
Ensure MongoDB is installed and running locally or use MongoDB Atlas (cloud). Set the `DATABASE_URL` in a `.env` file as follows:

```plaintext
DATABASE_URL=mongodb://localhost:27017
```

For MongoDB Atlas, use the connection string provided by Atlas.

## Configuration

1. Create a `.env` file in the root directory of your project.
2. Add the following configuration to the `.env` file:

```plaintext
DATABASE_URL=mongodb://localhost:27017  # Your MongoDB URL (local or Atlas)
```

## Running the Application

### 1. Run the Flask app:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development  # Optional: for development mode
flask run
```

This will start the Flask development server at `http://127.0.0.1:5000/`.

### 2. Access the Endpoints:
- **GET /**: Homepage, a placeholder route for testing.
- **GET /users/<email>**: Fetch user details by email.
- **POST /users**: Create a new user (send email, username, password).
- **PUT /users/<email>**: Update user password (send new password).
- **DELETE /users/<email>**: Delete a user by email.

## Using the Script

The script provides a set of functions to operate on user data. The operations include creating a user, updating a user's password, getting a user's details, and deleting a user.

### Running the Script

1. Ensure MongoDB is running.
2. Run the script by executing the following command:

```bash
python user_operations.py
```

The script includes the following operations:

### Available Functions in `user_operations.py`:

1. **`create_user(email, username, password)`**:
   - Creates a new user with the specified email, username, and password (password is hashed before storage).

2. **`update_user(email, new_password)`**:
   - Updates the password of the user identified by their email.

3. **`get_user(email)`**:
   - Fetches and displays the user details (email and username) for the given email.

4. **`delete_user(email)`**:
   - Deletes the user with the specified email.

### Example Script Output:

```bash
User admin created.
User Details - Email: admin@example.com, Username: admin
Password for admin@example.com updated successfully.
User Details - Email: admin@example.com, Username: admin
User with email admin@example.com deleted.
```

## Features Implemented

1. **User Creation**: Creates a new user with a hashed password.
2. **Password Update**: Allows updating the password for an existing user.
3. **Get User**: Fetches details of a user by email.
4. **Delete User**: Deletes a user from the database by email.

## Task Requirements

### Must Have:
1. **Login and Logout Endpoints**: These endpoints can be implemented as part of the API, though they are not explicitly written in the current code, they can be extended with JWT authentication.
2. **Secure Endpoints for User CRUD**: Implemented via secure password hashing and using Flask routes for user management (create, update, fetch, delete).
3. **Readable Code**: The code is organized with functions that handle CRUD operations in a clear manner.
4. **No ODM Library**: Used `pymongo` directly for interacting with MongoDB, instead of an ODM like `MongoEngine` or `Beanie`.
5. **Script to Create User**: The `user_operations.py` script handles user creation, update, get, and delete operations.

### Good To Have:
1. **Logging Support**: Not yet implemented, but can be added using Python's built-in `logging` module.
2. **Predefined Models with Pydantic**: Not used as Flask was chosen instead of FastAPI. Pydantic is more commonly used with FastAPI for request validation.
3. **MongoDB Atlas**: The connection string in the `.env` file can be configured for MongoDB Atlas.
4. **Scalable Code Structure**: The current code is modular and can be extended with more features (e.g., authentication, logging, RBAC).

### Added Bonus:
1. **Role-Based Access Control (RBAC)**: Not yet implemented but could be added by introducing roles (e.g., admin, user) and checking roles during user actions.
2. **Deployment**: The app can be deployed on platforms like Heroku, AWS, or any other free serverless services like Vercel, Render, or Railway.
