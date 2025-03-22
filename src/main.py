from fastapi import FastAPI, Request
import os
import uvicorn
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
import pages, news, engines, formsRegAndLogin
from operations_with_db import router as operations_router
from functions import router as functions_router
from formsRegAndLogin import router as forms_router 
from google_function import router as google_router

app = FastAPI()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_cookie = request.cookies.get("auth", "false")
        request.state.is_authenticated = auth_cookie == "true"
        response = await call_next(request)
        return response

app.add_middleware(AuthMiddleware)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(formsRegAndLogin.router)
app.include_router(pages.router)
app.include_router(news.router)
app.include_router(engines.router)
app.include_router(operations_router)
app.include_router(functions_router)
app.include_router(forms_router)
app.include_router(google_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)