import databases
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from datetime import datetime
# from passlib


load_dotenv()

user = getenv('DB_USER')
password = getenv('DB_PASS')
host = getenv('DB_HOST')
dbname = getenv('DB_NAME')

conn_str = f"""postgresql://{user}:{password}@{host}:5432/{dbname}"""

engine = create_engine(conn_str)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


async def get_user(session: Session, username: str) -> User:
    res = session.query(User).filter(User.username == username).first()
    session.close()
    return res


# Base.metadata.create_all(bind=engine)