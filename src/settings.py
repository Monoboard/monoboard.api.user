"""This module provides config variables for app."""

import os

# App stuff
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

# Database stuff
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "monoboard")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "monoboard-password")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "monoboard")
DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{database_name}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    database_name=POSTGRES_DB_NAME
)
