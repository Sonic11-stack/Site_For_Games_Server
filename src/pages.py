from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import Query

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/first_page")
async def first_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("First_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/second_page")
async def second_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Second_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/third_page")
async def third_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Third_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/fourth_page")
async def fourth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Fourth_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/fifth_page")
async def fifth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Fifth_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/sixth_page")
async def sixth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("Sixth_Page.html", {"request": request, "is_authenticated": is_authenticated})
