from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/game_engines")
async def game_engine(request: Request):
    return templates.TemplateResponse("Game_Engines.html", {"request": request})