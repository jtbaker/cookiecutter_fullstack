from fastapi import APIRouter, Depends, Response
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer
from passlib.registry import _name_re
from src.security.authentication import create_access_token, authenticate_user, create_user
from src.db.models import get_db
from sqlalchemy.orm import Session

# from .types import SignUpForm
# from ..security import authenticate_user
# from ..security.security import authenticate_user
router = APIRouter()

@router.post("/register")
async def register(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await create_user(db, username=form.username, password=form.password)
    return Response(content=f"Success: {form.username}, {form.password}.", status_code=status.HTTP_201_CREATED)
    
    

# @router.post("/signup")
# async def signup(form: SignUpForm):
#     return {"username": form.username, "email": form.email}

# @router.post("/signin"):
    