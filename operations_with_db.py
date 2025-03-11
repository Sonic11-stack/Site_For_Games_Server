from dependencies import FastAPI, Request, Depends, templates, os, get_db_connection, BaseHTTPMiddleware, StaticFiles, JSONResponse, Form, Body, RedirectResponse, APIRouter
import formsRegAndLogin

def get_db():
    conn = get_db_connection()
    try:
        yield conn  
    finally:
        conn.close()

router = APIRouter()

@router.get("/game/{game_id}")
async def get_game_page(request: Request, game_id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name, date, description, developer, publishers, platforms, sources_to_game, tags, logo FROM "InfoPage" WHERE id = %s', (game_id,))
    game = cur.fetchone()

    email = request.cookies.get("email")
    is_clicked = False

    if email:
        cur.execute('SELECT save_game FROM "Users" WHERE email = %s', (email,))
        user_data = cur.fetchone()
        if user_data and user_data['save_game']:
            saved_games = user_data['save_game'].split(',')
            is_clicked = str(game_id) in saved_games

    cur.execute('SELECT c.comment_id, c.comment, u.name FROM "Comments" c JOIN "Users" u ON c.email = u.email WHERE c.id = %s ORDER BY c.comment_id DESC', (game_id,))
    comments = cur.fetchall()
    cur.close()
    
    tags = game['tags']
    if isinstance(tags, str):
        tags_list = tags.split(", ")[:3]
    
    tag1 = tags_list[0]
    tag2 = tags_list[1]
    tag3 = tags_list[2]

    image_url = f"/static/images/Game_{game_id}.jpg"
    logo = game['logo']
    logo_1 = f"/static/icons/{logo}.jpg"
    text = game["name"]
    print("DEBUG:", game)

    if not game:
        return JSONResponse({"error": "Игра не найдена"}, status_code=404)
    
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse(
        "Game_Page.html",
        {"request": request, "name": game["name"] if isinstance(game, dict) else game[0], "game_id": game_id, "is_clicked": is_clicked, "logo": logo_1,
        "date": game["date"], "description": game["description"], "developer": game["developer"],
        "publishers": game["publishers"], "platforms": game["platforms"], "sources_to_game": game["sources_to_game"], 
        "tag1": tag1, "tag2": tag2, "tag3": tag3, "image_url": image_url, "is_authenticated": is_authenticated, "text": text, "comments": comments})

@router.get("/game_engine/{engine_id}")
async def get_game_page(request: Request, engine_id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name, date, description, developer, development, platforms, sources_to_game_engine, logo FROM "GameEngines" WHERE id = %s', (engine_id,))
    engine = cur.fetchone()
    cur.close()

    image_url = f"/static/images/Game_Engine_{engine_id}.jpg"
    logo = engine['logo']
    logo_1 = f"/static/icons/{logo}.jpg"
    print("DEBUG:", engine)

    if not engine:
        return JSONResponse({"error": "Игровой движок не найдена"}, status_code=404)
    
    is_authenticated = request.cookies.get("auth") == "true"

    return templates.TemplateResponse(
        "Game_Engine_Page.html",
        {"request": request, "name": engine["name"] if isinstance(engine, dict) else engine[0], 
         "date": engine["date"], "description": engine["description"], "developer": engine["developer"], "logo": logo_1,
        "development": engine["development"], "platforms": engine["platforms"], "sources_to_game_engine": engine["sources_to_game_engine"],
        "image_url": image_url, "is_authenticated": is_authenticated}
    )

@router.get("/news/{news_id}")
async def get_game_page(request: Request, news_id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT text_news, name, main_text FROM "News" WHERE id = %s', (news_id,))
    engine = cur.fetchone()
    cur.close()

    image_url = f"/static/images/Game_Engine_{news_id}.jpg"
    print("DEBUG:", engine)

    if not engine:
        return JSONResponse({"error": "Игровой движок не найдена"}, status_code=404)
    
    is_authenticated = request.cookies.get("auth") == "true"

    return templates.TemplateResponse(
        "New_Page.html",
        {"request": request, "name": engine["name"] if isinstance(engine, dict) else engine[0], 
        "image_url": image_url, "is_authenticated": is_authenticated}
    )

@router.get("/get_text_news/{id}")
async def get_game_page(request: Request, id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT text_news FROM "News" WHERE id = %s', (id,))
    text = cur.fetchone()
    text_1 = text['text_news'] if text else None
    cur.close()
    db.close()
    return JSONResponse(content={"text": text_1})

@router.get("/get_text/{id}")
async def get_game_page(request: Request, id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name FROM "InfoPage" WHERE id = %s', (id,))
    text = cur.fetchone()
    text_1 = text['name'] if text else None
    cur.close()
    db.close()
    return JSONResponse(content={"text": text_1})

@router.get("/get_text_engine/{id}")
async def get_game_page(request: Request, id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name FROM "GameEngines" WHERE id = %s', (id,))
    text = cur.fetchone()
    text_1 = text['name'] if text else None
    cur.close()
    db.close()
    return JSONResponse(content={"text": text_1})

@router.post("/click_button")
async def get_game_page(request: Request, name: str = Form(...), surname: str = Form(...), email: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('INSERT INTO "Users" (id, name, surname, email, password) VALUES (DEFAULT, %s, %s, %s, %s)', (name, surname, email, password))
    db.commit()
    cur.close()
    return templates.TemplateResponse("First_Page.html", {"request": request, "name": name, "surname": surname, "email": email, "password": password})

@router.post("/click_button_1")
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

@router.get("/profile")
async def profile(request: Request, db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('SELECT name, email, save_game, about_yourself, location FROM "Users" WHERE email = %s', (email,))
    user = cur.fetchone()
    cur.close()

    if not user:
        return RedirectResponse(url="/first_page", status_code=303)

    name_game = user["name"]
    bio = user["about_yourself"]
    location = user["location"]
    save_game_str = user["save_game"] if user["save_game"] else ""
    save_games = [int(game_id) for game_id in save_game_str.split(",") if game_id.isdigit()]
    is_authenticated = request.cookies.get("auth") == "true"
    image_urls = [f"/static/images/Game_{game_id}.jpg" for game_id in save_games]
    return templates.TemplateResponse("Profile.html", {"request": request, "user": user, "name_game": name_game, "bio": bio, "location": location, "is_authenticated": is_authenticated, "save_games": save_games, "image_urls": image_urls})

@router.post("/save_profile")
async def profile(request: Request, name: str = Form(...), bio: str = Form(...), location: str = Form(...), db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('UPDATE "Users" SET name = %s, about_yourself = %s, location = %s WHERE email = %s RETURNING *', (name, bio, location, email))
    db.commit()
    user = cur.fetchone()
    cur.close()
    return RedirectResponse(url="/profile", status_code=303)

@router.post("/click_star")
async def profile(request: Request, save_game: dict = Body(...), db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()

    cur.execute('SELECT save_game FROM "Users" WHERE email = %s', (email,))
    user_data = cur.fetchone()
    
    current_saves = user_data['save_game'] if user_data['save_game'] else ""
    game_id = str(save_game['save_game'])
    
    if current_saves:
        saved_games = current_saves.split(",")
        if game_id in saved_games:
            saved_games.remove(game_id)
            new_saves = ",".join(saved_games)
            is_clicked = False
        else:
            new_saves = f"{current_saves},{game_id}"
            is_clicked = True
    else:
        new_saves = game_id
        is_clicked = True
    
    cur.execute('UPDATE "Users" SET save_game = %s WHERE email = %s', (new_saves, email))
    db.commit()
    cur.close()
    
    return JSONResponse(content={"status": "success", "is_clicked": is_clicked})

@router.post("/stay_comment/{id}")
async def stay_comment(request: Request, id: int, comment: dict = Body(...), db=Depends(get_db)):
    email = request.cookies.get("email")
    cur = db.cursor()
    cur.execute('SELECT name FROM "Users" WHERE email = %s', (email,))
    user = cur.fetchone()
    
    cur.execute('INSERT INTO "Comments" (email, comment, id) VALUES (%s, %s, %s) RETURNING comment_id', 
                (email, comment["comment"], id))
    new_comment_id = cur.fetchone()['comment_id']
    db.commit()
    cur.close()
    
    return JSONResponse(content={
        "status": "success", 
        "comment": comment["comment"],
        "comment_id": new_comment_id,
        "author": user['name']
    })