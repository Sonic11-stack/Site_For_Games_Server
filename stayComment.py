from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
import sqlite3

app = FastAPI()

# Подключение к базе данных SQLite
def connect_db():
    conn = sqlite3.connect("Comments.db")
    conn.row_factory = sqlite3.Row
    return conn

# Создаем таблицу, если ее нет
def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            comment TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

setup_db()

# Модель данных
class Comment(BaseModel):
    name: str
    email: EmailStr
    comment: str

# Маршрут для добавления комментария
@app.post("/add_comment")
async def add_comment(comment: Comment):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Comments (name, email, comment) VALUES (?, ?, ?)",
        (comment.name, comment.email, comment.comment)
    )
    conn.commit()
    conn.close()
    return {"message": "Комментарий добавлен"}

# Маршрут для получения комментариев
@app.get("/get_comments")
async def get_comments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, comment FROM Comments")
    rows = cursor.fetchall()
    conn.close()
    return JSONResponse(content=[
        {"id": row["id"], "name": row["name"], "email": row["email"], "comment": row["comment"]}
        for row in rows
    ])
