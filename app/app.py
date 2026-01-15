from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from markupsafe import Markup
from backend import main

#api_key = os.environ.get('API_KEY')
api_key = "915657d4de9518c7ed7dc042dd08050606fa1492"

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/zip/{zipcode}/years/{minYear}-{maxYear}')
async def zipyear(zipcode: str | None, minYear: int | None, maxYear: int | None):
    plot_html = main.execute(api_key, zipcode, minYear, maxYear)
    return HTMLResponse(content=plot_html)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

# Move variable and CSV selection to page
# Export CSV functionality
# Loading view
# Pretty with CSS