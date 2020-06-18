from pydantic import BaseModel


class SignUpForm(BaseModel):
    username: str
    email: str
    password: str