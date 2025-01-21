from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import pages, news, engines, formsRegAndLogin, games, stayComment
from pydantic import BaseModel, EmailStr
import sqlite3

from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os

app = FastAPI()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  

GOOGLE_CLIENT_SECRET_FILE = "EnterGoogle.json"
GOOGLE_SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"  

@app.get("/auth/google")
async def auth_google():
    flow = Flow.from_client_secrets_file(
        GOOGLE_CLIENT_SECRET_FILE,
        scopes=GOOGLE_SCOPES,
        redirect_uri=REDIRECT_URI  
    )
    authorization_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(authorization_url)

@app.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        error = request.query_params.get("error")
        if error == "access_denied":
            return RedirectResponse(url="/login")
        return {"error": "Missing authorization code"}

    try:
        flow = Flow.from_client_secrets_file(
            GOOGLE_CLIENT_SECRET_FILE,
            scopes=GOOGLE_SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(code=code)

        credentials = flow.credentials
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()

        if user_info.get("verified_email"):
            return RedirectResponse(url="/first_page")
        else:
            return RedirectResponse(url="/error_page")

    except Exception as e:
        return {"error": f"Internal server error: {str(e)}"}

app.include_router(pages.router)
app.include_router(news.router)
app.include_router(engines.router)
app.include_router(formsRegAndLogin.router)
app.include_router(games.router)

def connect_db():
    conn = sqlite3.connect("Comments.db")
    conn.row_factory = sqlite3.Row
    return conn

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

class Comment(BaseModel):
    name: str
    email: EmailStr
    comment: str

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


app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
