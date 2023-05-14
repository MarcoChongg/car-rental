from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db.db_setup import engine

router = APIRouter()


templates = Jinja2Templates(directory="./templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@router.get("/login", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Sign In"
    }
    return templates.TemplateResponse("login.html", {"request": request, "data": data})