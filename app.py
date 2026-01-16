from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from backend import main
from functools import lru_cache
import os

api_key = os.environ.get('API_KEY')

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@lru_cache(maxsize=32)
def pull_data(zipcode: str, minYear: int, maxYear: int):
    return main.execute_df(api_key, zipcode, minYear, maxYear)

@app.post("/load/zip/{zipcode}/years/{minYear}-{maxYear}")
async def df_cache(zipcode: str, minYear: int, maxYear: int):
    pull_data(zipcode, minYear, maxYear)

@app.get('/viz/zip/{zipcode}/years/{minYear}-{maxYear}/var/{variable}')
async def viz(zipcode: str, minYear: int, maxYear: int, variable: str):
    df, year_len = pull_data(zipcode, minYear, maxYear)
    plot_html = main.execute_viz(df, year_len, variable)
    return HTMLResponse(content=plot_html)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)

# Fix housing value >million bug
# Move variable and CSV selection to page
# Export CSV functionality
# Loading view
# Pretty with CSS
# upload to Render