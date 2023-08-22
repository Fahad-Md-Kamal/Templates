import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@database:5432/fastapi_db")
engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()















# import os

# import sqlalchemy
# from databases import Database

# DATABASE_URL = os.environ["DATABASE_URL"]#"postgresql+psycopg2://postgres:postgres@database:5432/fastapi_db"
# # DATABASE_URL = "sqlite:///sqlite3.db"
# database = Database(DATABASE_URL)
# sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


# def get_database() -> Database:
#     return database


# metadata = sqlalchemy.MetaData()



