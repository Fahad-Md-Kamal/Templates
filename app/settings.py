import os

from dotenv import load_dotenv

load_dotenv(".env")

DATABASE_URL = os.environ.get("DATABASE_URL")
REDIS_HOST_URL = os.environ.get("REDIS_HOST_URL")
