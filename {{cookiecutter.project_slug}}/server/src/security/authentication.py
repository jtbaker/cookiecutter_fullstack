# import
from passlib.context import CryptContext
import jwt
import os
from server.src.db.models import User, get_user
from sqlalchemy.orm import Session
from typing import Union


# from .models import User, get_user
from datetime import datetime, timedelta

from dotenv import load_dotenv

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY", "none")

ACCESS_TOKEN_EXPIRE_MINUTES = (
    int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "0"))
    if os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") is not None
    else None
)

async def create_user(db: Session, username: str, password: str) -> User:
    hashed_pwd = pwd_context.hash(password)
    user = User(name=username, password=hashed_pwd)
    db.add(user)
    db.commit()
    return user


async def authenticate_user(
    session: Session,
    username: str, password: str, context: CryptContext = pwd_context
) -> Union[User, None]:
    user = await get_user(session, username)
    if not user:
        return None
    if not context.verify(password, user.password):
        return None
    return user


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES if ACCESS_TOKEN_EXPIRE_MINUTES is not None else 30),
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt
