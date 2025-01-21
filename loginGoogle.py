# Пример получения данных пользователя с помощью Google API OAuth2

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# pip install google-api-python-client google-auth-oauthlib

# Создаем проект в Google Cloud Platform
# https://console.cloud.google.com/cloud-resource-manager?authuser=1
# https://console.cloud.google.com/apis/credentials

from fastapi.responses import RedirectResponse

@app.get("/auth/google")
async def auth_google():
    flow = InstalledAppFlow.from_client_secrets_file(
        '../google/EnterGoogle.json',
        scopes=[
            'openid',
            'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile'
        ]
    )
    flow.redirect_uri = "http://127.0.0.1:8000/auth/google/callback"
    authorization_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(authorization_url)