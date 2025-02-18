from fastapi import FastAPI, Request, Response, Depends, Cookie
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import pages, news, engines, formsRegAndLogin, games, stayComment, sendEmail
from pydantic import BaseModel, EmailStr
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from games import router as games_router
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os

import psycopg2
from psycopg2.extras import RealDictCursor

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

app.include_router(formsRegAndLogin.router)

def get_db_connection():
    return psycopg2.connect(
        dbname="selecteldb",
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
    )
    
def get_db():
    conn = get_db_connection()
    try:
        yield conn  
    finally:
        conn.close()

@app.get("/game/{game_id}")
async def get_game_page(request: Request, game_id: int, db=Depends(get_db)):
    cur = db.cursor()
    
    cur.execute("SELECT name FROM InfoPage WHERE id = %s", (game_id,))
    game = cur.fetchone()
    cur.close()

    if not game:
        return JSONResponse({"error": "Игра не найдена"}, status_code=404)

    return templates.TemplateResponse(
        "game_page.html",
        {"request": request, "namePage": game[0]}
    )

@app.get("/profile")
async def profile(request: Request):
    return templates.TemplateResponse("Profile.html", {"request": request})

@app.post("/log")
async def log(response: Response):
    response.set_cookie(key="auth", value="true", httponly=True, path="/")
    return JSONResponse(content={"success": True, "message": "Вход выполнен"}, status_code=200)

@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie("auth", path="/") 
    return JSONResponse(content={"success": True, "message": "Выход выполнен"}, status_code=200)

@app.middleware("http")
async def add_no_cache_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

@app.get("/{path:path}")
async def universal_page(request: Request, path: str):
    if "." in path:  
        return JSONResponse({"error": "Not found"}, status_code=404)
    template_path = f"{path}.html"  
    return templates.TemplateResponse(template_path, {"request": request, "is_authenticated": request.state.is_authenticated})

@app.get("/news_first_page")
async def news_page():
    return {"message": "Страница новостей"}

app.include_router(games.router)
app.include_router(pages.router)
app.include_router(news.router)
app.include_router(engines.router)


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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)