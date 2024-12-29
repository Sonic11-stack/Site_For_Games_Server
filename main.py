from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

template = Jinja2Templates(directory = "templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def index(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/first_page")
def about_page(req: Request):
    return template.TemplateResponse("First_Page.html", {"request": req})

@app.get("/second_page")
def about_page(req: Request):
    return template.TemplateResponse("Second_Page.html", {"request": req})

@app.get("/third_page")
def about_page(req: Request):
    return template.TemplateResponse("Third_Page.html", {"request": req})

@app.get("/fourth_page")
def about_page(req: Request):
    return template.TemplateResponse("Fourth_Page.html", {"request": req})

@app.get("/fifth_page")
def about_page(req: Request):
    return template.TemplateResponse("Fifth_Page.html", {"request": req})

@app.get("/sixth_page")
def about_page(req: Request):
    return template.TemplateResponse("Sixth_Page.html", {"request": req})

if __name__ == "__main__":
    uvicorn.run("main:app")