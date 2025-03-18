from dependencies import Request, templates, os, JSONResponse, RedirectResponse, APIRouter
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
import os
import formsRegAndLogin

from fastapi import Request
from fastapi.responses import JSONResponse, RedirectResponse
import os

router = APIRouter()

@router.get("/open_explorer")
async def open_explorer(request: Request):
    os.startfile("C:\\Users")
    return RedirectResponse(url=request.url_for('profile'))

@router.get("/{path:path}")
async def universal_page(request: Request, path: str):
    if "." in path:  
        return JSONResponse({"error": "Not found"}, status_code=404)
    template_path = f"{path}.html"  
    return templates.TemplateResponse(template_path, {"request": request, "is_authenticated": request.state.is_authenticated})

@router.get("/news_first_page")
async def news_page():
    return {"message": "Страница новостей"}