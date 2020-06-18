# import
from passlib.context import CryptContext
import jwt
import os

import datetime

from dotenv import load_dotenv

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


async def authenticate_user(username: str, password: str, context: CryptContext pwd_context) -> User:
    user = await get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt
