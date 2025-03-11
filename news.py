from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/news_first_page")
async def news_first_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_First_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/news_second_page")
async def news_second_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_Second_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/news_third_page")
async def news_third_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_Third_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/news_fourth_page")
async def news_fourth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_Fourth_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/news_fifth_page")
async def news_fifth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_Fifth_Page.html", {"request": request, "is_authenticated": is_authenticated})

@router.get("/news_sixth_page")
async def news_sixth_page(request: Request):
    is_authenticated = request.cookies.get("auth") == "true"
    return templates.TemplateResponse("News_Sixth_Page.html", {"request": request, "is_authenticated": is_authenticated})
