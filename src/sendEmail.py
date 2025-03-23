from fastapi import FastAPI, Request, Response, Depends, Cookie
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import pages, engines, formsRegAndLogin
from pydantic import BaseModel, EmailStr
import sqlite3
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "" 
EMAIL_HOST_PASSWORD = "" 

verification_codes = {} 
def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email(email: str, code: str):
    def test_email_sending():
        test_email = ""
        test_code = generate_verification_code()
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = test_email
        msg['Subject'] = "Тестовый код подтверждения"
        body = f"Тестовый код подтверждения: {test_code}"
        msg.attach(MIMEText(body, 'plain'))
        
        print("Тестовое сообщение создано успешно")
        
        try:
            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            server.starttls()
            print("Подключение к SMTP серверу успешно")
            return True
        except Exception as e:
            print(f"Ошибка подключения к SMTP: {e}")
            return False
            
    if not test_email_sending():
        print("Тест не пройден, проверьте настройки SMTP")
        return False
        
    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = email
    msg['Subject'] = "Код подтверждения"
    
    body = f"Ваш код подтверждения: {code}"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email отправлен успешно")
        return True
    except Exception as e:
        print(f"Ошибка отправки email: {e}")
        return False

@app.post("/send-verification")
async def send_verification(email: EmailStr):
    if not "@" in email:
        return JSONResponse(content={"error": "Неверный формат email"}, status_code=400)
        
    code = generate_verification_code()
    verification_codes[email] = code
    
    if send_verification_email(email, code):
        return JSONResponse(content={"message": "Код подтверждения отправлен"})
    return JSONResponse(content={"error": "Ошибка отправки кода"}, status_code=500)

@app.post("/verify-code")
async def verify_code(email: EmailStr, code: str):
    if email not in verification_codes:
        return JSONResponse(content={"error": "Код не был отправлен"}, status_code=400)
        
    stored_code = verification_codes.get(email)
    if stored_code and stored_code == code:
        verification_codes.pop(email)
        return JSONResponse(content={"message": "Код подтвержден"})
    return JSONResponse(content={"error": "Неверный код"}, status_code=400)