from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import Request, Response

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/reg")
async def reg(request: Request):
    return templates.TemplateResponse("Registration.html", {"request": request})

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})

@router.post("/log")
async def log(response: Response):
    response.set_cookie(key="auth", value="true", httponly=True, path="/")
    return JSONResponse(content={"success": True, "message": "Вход выполнен"}, status_code=200)

@router.post("/logout")
async def logout(response: Response):
    response = JSONResponse(content={"success": True, "message": "Выход выполнен"}, status_code=200)
    response.delete_cookie(key="auth", path="/")
    response.delete_cookie(key="email", path="/")
    response.set_cookie(key="auth", value="false", httponly=True, path="/")
    return response

