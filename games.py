from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/the_last_of_us")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The Last Of Us.html", {"request": request})

@router.get("/the_last_of_us_2")
async def the_last_of_us(request: Request):
    return templates.TemplateResponse("The Last Of Us 2.html", {"request": request})