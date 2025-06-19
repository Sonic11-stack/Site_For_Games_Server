import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv() 

def get_db_connection():
     return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        cursor_factory=RealDictCursor
    )

def get_db_connection_1():
    return psycopg2.connect(
        api_key = os.getenv("RAWG_API_KEY"),
        dbname=os.getenv("DB_NAME_1"),
        user=os.getenv("DB_USER_1"),
        password=os.getenv("DB_PASSWORD_1"),
        host=os.getenv("DB_HOST_1"),
        port=os.getenv("DB_PORT_1"),
        cursor_factory=RealDictCursor
    )