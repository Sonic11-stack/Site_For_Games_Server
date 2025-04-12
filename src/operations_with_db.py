from dependencies import shutil, bcrypt, psycopg2, BaseModel, JSONResponse, RedirectResponse, APIRouter, File, UploadFile, Request, Depends, HTTPException, Form, Body
from db_utils import get_db_connection_1

def get_db():
    conn = get_db_connection_1()
    try:
        yield conn  
    finally:
        conn.close()

router = APIRouter()

class LoginData(BaseModel):
    email: str
    password: str

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed.decode()  

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    except ValueError:
        return False    



@router.get("/get_text/{id}")
async def get_game_page(request: Request, id: int, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute('SELECT name FROM "InfoPage" WHERE id = %s', (id,))
    text = cur.fetchone()
    text_1 = text['name'] if text else None
    cur.close()
    return JSONResponse(content={"text": text_1})


    
@router.get("/")
async def root(request: Request):
    return templates.TemplateResponse("First_Page.html", {"request": request})
    