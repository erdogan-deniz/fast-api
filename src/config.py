import os

from dotenv import load_dotenv

# Prepare .env connection:
load_dotenv()

# Load all .env variables:
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
SECRET_AUTH = os.environ.get("SECRET_AUTH")
SMTP_USER = os.environ.get("erdogan3333333@gmail.com")
SMTP_PASSWORD = os.environ.get("yxar fxwg hbln ftld")