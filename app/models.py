from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    email = db.StringField(unique=True, required=True)
    name = db.StringField(required=True)
    password = db.StringField(required=True)

    def to_json(self):
        return {
            "email": self.email,
            "name": self.name,
            "password": self.password  # In a real-world app, avoid sending passwords like this
        }
