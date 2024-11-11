import jwt
from datetime import datetime, timedelta
from app.config import config

def create_jwt_token(data: dict) -> str:
    payload = {
        **data,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)

def decode_jwt_token(token: str) -> dict:
    return jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
