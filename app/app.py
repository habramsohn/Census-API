from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import backend

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/zip/{zipcode}/years/{minYear}-{maxYear}')
async def zipyear(zipcode: int, minYear: int, maxYear):
    plot_html = execute()
    return {"status": "Success", "plot": plot_html}