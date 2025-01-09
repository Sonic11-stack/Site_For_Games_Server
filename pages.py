from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/first_page")
async def first_page(request: Request):
    return templates.TemplateResponse("First_Page.html", {"request": request})

@router.get("/second_page")
async def second_page(request: Request):
    return templates.TemplateResponse("Second_Page.html", {"request": request})

@router.get("/third_page")
async def third_page(request: Request):
    return templates.TemplateResponse("Third_Page.html", {"request": request})

@router.get("/fourth_page")
async def fourth_page(request: Request):
    return templates.TemplateResponse("Fourth_Page.html", {"request": request})

@router.get("/fifth_page")
async def fifth_page(request: Request):
    return templates.TemplateResponse("Fifth_Page.html", {"request": request})

@router.get("/sixth_page")
async def sixth_page(request: Request):
    return templates.TemplateResponse("Sixth_Page.html", {"request": request})
