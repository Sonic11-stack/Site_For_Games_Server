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
from fastapi import APIRouter

templates = Jinja2Templates(directory="templates")

def get_db_connection():
    return psycopg2.connect(
        dbname="Info",
        user="postgres",
        password="Beripal826har",
        host="127.0.0.1",
        port="5432",
        cursor_factory=RealDictCursor
    )