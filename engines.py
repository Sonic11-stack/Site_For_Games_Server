from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/game_engine")
async def game_engine(request: Request):
    return templates.TemplateResponse("Game_Engines.html", {"request": request})

@router.get("/unity")
async def unity(request: Request):
    return templates.TemplateResponse("Unity.html", {"request": request})

@router.get("/unreal_engine")
async def unreal_engine(request: Request):
    return templates.TemplateResponse("Unreal_Engine.html", {"request": request})

@router.get("/godot")
async def godot(request: Request):
    return templates.TemplateResponse("Godot.html", {"request": request})


