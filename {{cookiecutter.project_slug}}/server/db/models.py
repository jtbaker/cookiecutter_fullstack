import databases
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from datetime import datetime
# from passlib


load_dotenv()

user = getenv('dbuser')
password = getenv('dbpass')
host = getenv('host')
dbname = getenv('dbname')

conn_str = f"""postgresql://{user}:{password}@{host}:5432/{dbname}"""

engine = create_engine("postgresql://postgres:postgres@pg:5432/postgres")

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class User(Base): # type: ignore
    __tablename__ = "users"
    id: int = Column('id', sqlalchemy.Integer, primary_key=True)
    name: str = Column('name', sqlalchemy.Text)
    password: str = Column('password', sqlalchemy.Text)
    email: str = Column('email', sqlalchemy.Text)
    created: datetime = Column('created', sqlalchemy.TIMESTAMP)
    last_login: datetime = Column('last_login', sqlalchemy.TIMESTAMP)

    def create(self, name: str, email: str, password: str):
        return self.__init__(name=name, email=email, password=password)

    # def hash_password():

    # def verify_password():


async def get_user(username: str) -> User:
    session = Session()
    res = session.query(User).filter(User.username == username).first()
    session.close()
    return res

