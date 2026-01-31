from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import uvicorn
from backend import main
from functools import lru_cache
import os
import io

# API contained in Render
api_key = "915657d4de9518c7ed7dc042dd08050606fa1492"
#os.environ.get("API_KEY")

# FastAPI connecting backend and HTML/JS
app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


# Landing page
@app.get("/", response_class=HTMLResponse)
async def get_landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Generate cache when dataset requested to prevent reloading
@lru_cache(maxsize=32)
def pull_data(api_key, zipcode: str, minYear: int, maxYear: int):
    return main.execute_df(api_key, zipcode, minYear, maxYear)


# Trigger API call when URL passed
@app.post("/load/zip/{zipcode}/years/{minYear}-{maxYear}")
async def df_cache(zipcode: str, minYear: int, maxYear: int):
    pull_data(api_key, zipcode, minYear, maxYear)


# Generate CSV when export requested
@app.get("/load/zip/{zipcode}/years/{minYear}-{maxYear}/export")
async def export_csv(zipcode: str, minYear: int, maxYear: int):
    df, year_len = pull_data(api_key, zipcode, minYear, maxYear)
    export_df = main.export_csv(df)
    # Use io package to stream dynamic data based on URL
    stream = io.StringIO()
    export_df.to_csv(stream, index=True)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    # Attach CSV to page with specified name
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response


# Pull visualization logic with requested variable through custom URL 
@app.get("/viz/zip/{zipcode}/years/{minYear}-{maxYear}/var/{variable}")
async def viz(zipcode: str, minYear: int, maxYear: int, variable: str):
    df, year_len = pull_data(api_key, zipcode, minYear, maxYear)
    # See backend/main.py
    plot_html = main.execute_viz(df, year_len, variable)
    return HTMLResponse(content=plot_html)


# Uvicorn as agent to host on Render
if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 10000))
    #uvicorn.run("app:app", host="0.0.0.0", port=port)
    # Local testing
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
