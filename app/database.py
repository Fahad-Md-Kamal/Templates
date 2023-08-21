import os

import sqlalchemy
from databases import Database

DATABASE_URL = os.environ["DATABASE_URL"]#"postgresql+psycopg2://postgres:postgres@database:5432/fastapi_db"
# DATABASE_URL = "sqlite:///sqlite3.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


def get_database() -> Database:
    return database


metadata = sqlalchemy.MetaData()
