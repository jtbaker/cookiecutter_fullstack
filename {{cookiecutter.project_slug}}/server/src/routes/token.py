from server.src.routes.crud import pwd_context
from fastapi import APIRouter, Depends
from argon2 import PasswordHasher
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
from os import environ
import jwt
# from main import SECRET_KEY
from datetime import datetime, timedelta
from server.src.db.models import User, get_db
from sqlalchemy.orm import Session

# Session


SECRET_KEY = environ["SECRET_KEY"]

pwd_context = CryptContext(schemes=['argon2'])


def validate_user(session: Session, username: str, password: str):
    # session = Session()
    user: User = session.query(User).filter(User.username==username).first()
    if user:
        return pwd_context.verify(password, user.password)
    else:
        return False


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

router = APIRouter()


@router.post("/token", response_model=str)
async def authenticate(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    return 'test'
