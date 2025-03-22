from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

router = APIRouter()

GOOGLE_CLIENT_SECRET_FILE = "EnterGoogle.json"
GOOGLE_SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

@router.get("/auth/google")
async def auth_google():
    flow = Flow.from_client_secrets_file(
        GOOGLE_CLIENT_SECRET_FILE,
        scopes=GOOGLE_SCOPES,
        redirect_uri=REDIRECT_URI  
    )
    authorization_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(authorization_url)

@router.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        error = request.query_params.get("error")
        if error == "access_denied":
            return RedirectResponse(url="/login")
        return {"error": "Missing authorization code"}
    try:
        flow = Flow.from_client_secrets_file(
            GOOGLE_CLIENT_SECRET_FILE,
            scopes=GOOGLE_SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(code=code)

        credentials = flow.credentials
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()

        if user_info.get("verified_email"):
            return RedirectResponse(url="/first_page")
        else:
            return RedirectResponse(url="/error_page")

    except Exception as e:
        return {"error": f"Internal server error: {str(e)}"}