from dependencies import FastAPI, Request, templates, os, BaseHTTPMiddleware, StaticFiles, JSONResponse, RedirectResponse, APIRouter
import formsRegAndLogin
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
import formsRegAndLogin

from fastapi import FastAPI, Request, Response, Depends, Form, Body
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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