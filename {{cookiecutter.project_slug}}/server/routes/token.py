from fastapi import APIRouter, Depends
from argon2 import PasswordHasher
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

router = APIRouter()


@router.post("/token", response_model=str)
async def authenticate(form: OAuth2PasswordRequestForm = Depends()):
    return 'test'
