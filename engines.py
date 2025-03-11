from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/game_engines")
async def game_engine(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Game_Engines.html", {"request": request, "is_authenticated": is_authenticated})