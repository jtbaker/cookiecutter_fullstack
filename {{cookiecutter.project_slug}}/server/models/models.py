import databases
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()

user = getenv('dbuser')
password = getenv('dbpass')
host = getenv('host')
dbname = getenv('dbname')

conn_str = f"""postgresql://{user}:{password}@{host}:5432/{dbname}"""

engine = create_engine(conn_str)

Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column('id', sqlalchemy.Integer, primary_key=True)
    name = Column('name', sqlalchemy.Text)
    password = Column('password', sqlalchemy.Text)
    email = Column('email', sqlalchemy.Text)
    created = Column('created', sqlalchemy.TIMESTAMP)
    last_login = Column('last_login', sqlalchemy.TIMESTAMP)

    def create(name: str, email: str, password: str):
        return None


async def get_user(username: str) -> User:
    session = Session()
    res = session.query(User).filter(User.username == username).first()
    session.close()
    return res
