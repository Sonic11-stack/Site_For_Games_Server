from fastapi import FastAPI, Request, Response, Depends, Cookie
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import pages, news, engines, formsRegAndLogin, games, stayComment
from pydantic import BaseModel, EmailStr
import sqlite3
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware


from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_cookie = request.cookies.get("auth", "false")
        request.state.is_authenticated = auth_cookie == "true"
        response = await call_next(request)
        return response

app.add_middleware(AuthMiddleware)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/log")
async def log(response: Response):
    response.set_cookie(key="auth", value="true", httponly=True, path="/")
    return JSONResponse(content={"success": True, "message": "Вход выполнен"}, status_code=200)

@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie("auth", path="/") 
    return JSONResponse(content={"success": True, "message": "Выход выполнен"}, status_code=200)

@app.get("/{path:path}")
async def universal_page(request: Request, path: str):
    if "." in path:  
        return JSONResponse({"error": "Not found"}, status_code=404)
    template_path = f"{path}.html"  
    return templates.TemplateResponse(template_path, {"request": request, "is_authenticated": request.state.is_authenticated})

@app.get("/reg")
async def registration_page():
    return {"message": "Страница регистрации"}

@app.get("/news_first_page")
async def news_page():
    return {"message": "Страница новостей"}

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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
