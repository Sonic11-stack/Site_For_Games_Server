from dependencies import Request, templates, JSONResponse, APIRouter

router = APIRouter()

@router.get("/{path:path}")
async def universal_page(request: Request, path: str):
    if "." in path:  
        return JSONResponse({"error": "Not found"}, status_code=404)
    template_path = f"{path}.html"  
    return templates.TemplateResponse(template_path, {"request": request, "is_authenticated": request.state.is_authenticated})

@router.get("/news_first_page")
async def news_page():
    return {"message": "Страница новостей"}