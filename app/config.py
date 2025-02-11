import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), './docker/.env')
load_dotenv(dotenv_path)

DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = os.environ.get("DB_URL")
DB_HOST = os.environ.get("DB_HOST")