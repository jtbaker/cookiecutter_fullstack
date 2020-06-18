from fastapi import APIRouter
from .types import SignUpForm

router = APIRouter()



@router.post("/signup")
async def signup(form: SignUpForm):
    return {"username": form.username, "email": form.email}

@router.post("/signin"):
    