import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
GITHUB_SECRET = os.environ.get("GITHUB_SECRET")

PUB_KEY_PATH = os.environ.get("PUB_KEY_PATH")
PRIV_KEY_PATH = os.environ.get("PRIV_KEY_PATH")
