import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname="Info",
        user="postgres",
        password="Beripal826har",
        host="127.0.0.1",
        port="5432",
        cursor_factory=RealDictCursor
    )