from fastapi import FastAPI, Request, Response, Depends, Form
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import pages, news, engines, formsRegAndLogin, games
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from games import router as games_router
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
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
        dbname="InfoPages",
        user="postgres",
        password="Beripal826har",
        host="127.0.0.1",
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
    cur.execute('SELECT name, date, description, developer, publishers, platforms, sources_to_game, tags FROM "InfoPage" WHERE id = %s', (game_id,))
    game = cur.fetchone()
    cur.close()
    
    tags = game['tags']
    if isinstance(tags, str):
        tags_list = tags.split(", ")[:3]
    
    tag1 = tags_list[0]
    tag2 = tags_list[1]
    tag3 = tags_list[2]

    image_url = f"/static/images/Game_{game_id}.jpg"
    print("DEBUG:", game)

    if not game:
        return JSONResponse({"error": "Игра не найдена"}, status_code=404)
    
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse(
        "Game_Page.html",
        {"request": request, "name": game["name"] if isinstance(game, dict) else game[0], 
        "date": game["date"], "description": game["description"], "developer": game["developer"],
        "publishers": game["publishers"], "platforms": game["platforms"], "sources_to_game": game["sources_to_game"], 
        "tag1": tag1, "tag2": tag2, "tag3": tag3, "image_url": image_url, "is_authenticated": is_authenticated})
    
@app.get("/game_engine/{engine_id}")
async def get_game_page(request: Request, engine_id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name, date, description, developer, development, platforms, sources_to_game_engine FROM "GameEngines" WHERE id = %s', (engine_id,))
    engine = cur.fetchone()
    cur.close()

    image_url = f"/static/images/Game_Engine_{engine_id}.jpg"
    print("DEBUG:", engine)

    if not engine:
        return JSONResponse({"error": "Игровой движок не найдена"}, status_code=404)
    
    is_authenticated = request.cookies.get("auth") == "true"

    return templates.TemplateResponse(
        "Game_Engine_Page.html",
        {"request": request, "name": engine["name"] if isinstance(engine, dict) else engine[0], 
         "date": engine["date"], "description": engine["description"], "developer": engine["developer"],
        "development": engine["development"], "platforms": engine["platforms"], "sources_to_game_engine": engine["sources_to_game_engine"],
        "image_url": image_url, "is_authenticated": is_authenticated}
    )

@app.post("/click_button")
async def get_game_page(request: Request, name: str = Form(...), surname: str = Form(...), email: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('INSERT INTO "Users" (id, name, surname, email, password) VALUES (DEFAULT, %s, %s, %s, %s)', (name, surname, email, password))
    db.commit()
    cur.close()
    return templates.TemplateResponse("First_Page.html", {"request": request, "name": name, "surname": surname, "email": email, "password": password})

@app.post("/click_button_1")
async def get_game_page(request: Request, email: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT email, password FROM "Users" WHERE email = %s AND password = %s', (email, password))
    user = cur.fetchone()

    if not user:
        cur.close()
        db.close()
        return {"error": "Пользователь не найден"}

    db.commit()
    cur.close()
    
    response = RedirectResponse(url="/first_page", status_code=303)
    response.set_cookie(key="auth", value="true", httponly=True, path="/")
    response.set_cookie(key="email", value=email, httponly=True, path="/")
    return response

@app.get("/profile")
async def profile(request: Request, db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('SELECT name, email, save_game FROM "Users" WHERE email = %s', (email,))
    user = cur.fetchone()
    cur.close()
    name_game = user["name"]
    save_game_str = user["save_game"] if user["save_game"] else ""
    save_games = [int(game_id) for game_id in save_game_str.split(",") if game_id.isdigit()]
    is_authenticated = request.cookies.get("auth") == "true"
    image_urls = [f"/static/images/Game_{game_id}.jpg" for game_id in save_games]
    return templates.TemplateResponse("Profile.html", {"request": request, "user": user, "name_game": name_game, "is_authenticated": is_authenticated, "save_games": save_games, "image_urls": image_urls})

@app.post("/save_profile")
async def profile(request: Request, name: str = Form(...), db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('UPDATE "Users" SET name = %s WHERE email = %s RETURNING *', (name,email))
    db.commit()
    user = cur.fetchone()
    cur.close()
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Profile.html", {"request": request, "user": user, "is_authenticated": is_authenticated, "name": name})

@app.post("/click_star")
async def profile(request: Request,response: Response, db=Depends(get_db)):
    is_authenticated = request.cookies.get("auth") == "true"
    is_clicked = True
    return JSONResponse(content={"status": "success", "is_clicked": is_clicked})

@app.post("/stay_comment")
async def stay_comment(request: Request, comment: str = Form(...), db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('INSERT INTO "Comments" (email, comment) VALUES (%s, %s)', (email, comment))
    db.commit()
    cur.close()
    return JSONResponse(content={"status": "success", "comment": comment})

@app.post("/log")
async def log(response: Response):
    response.set_cookie(key="auth", value="true", httponly=True, path="/")
    return JSONResponse(content={"success": True, "message": "Вход выполнен"}, status_code=200)

@app.post("/logout")
async def logout(response: Response):
    response = JSONResponse(content={"success": True, "message": "Выход выполнен"}, status_code=200)
    response.delete_cookie(key="auth", path="/")
    response.delete_cookie(key="email", path="/")
    response.set_cookie(key="auth", value="false", httponly=True, path="/")
    return response

@app.middleware("http")
async def add_no_cache_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

@app.get("/open_explorer")
async def open_explorer(request: Request):
    os.startfile("C:\\Users")
    return RedirectResponse(url=request.url_for('profile'))

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