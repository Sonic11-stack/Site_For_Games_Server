from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/the_last_of_us")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The Last Of Us.html", {"request": request})

@router.get("/the_last_of_us_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The_Last_of_Us_2.html", {"request": request})

@router.get("/horizon_zero_dawn")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Horizon_Zero_Dawn.html", {"request": request})

@router.get("/horizon_forbidden_west")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Horizon_Forbidden_West.html", {"request": request})

@router.get("/mass_effect")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect.html", {"request": request})

@router.get("/mass_effect_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect_2.html", {"request": request})

@router.get("/mass_effect_3")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("Mass_Effect_3.html", {"request": request})