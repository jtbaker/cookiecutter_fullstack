from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import timedelta, datetime
import jwt
from db.models import User

pwd_context = CryptContext(schemes=['argon2'])

router = APIRouter()

# def authenticate_user(username, password):


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt



# @router.post("/authenticate")
# async def authenticate(form: OAuth2PasswordRequestForm = Depends()):
    