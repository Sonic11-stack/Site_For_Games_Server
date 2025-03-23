from fastapi import FastAPI, Request, Response, Depends, Form, Body
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter
import uvicorn
import pages, engines, formsRegAndLogin

import shutil
import bcrypt
import psycopg2
from pydantic import BaseModel
from fastapi import File, HTTPException, UploadFile

templates = Jinja2Templates(directory="templates")

from operations_with_db import router as operations_router
from functions import router as functions_router
from formsRegAndLogin import router as forms_router 
from google_function import router as google_router
