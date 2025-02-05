from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/reg")
async def reg(request: Request):
    return templates.TemplateResponse("Registration.html", {"request": request})

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})

