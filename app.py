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

api_key = os.environ.get('API_KEY')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@lru_cache(maxsize=32)
def pull_data(api_key, zipcode: str, minYear: int, maxYear: int):
    return main.execute_df(api_key, zipcode, minYear, maxYear)

@app.post("/load/zip/{zipcode}/years/{minYear}-{maxYear}")
async def df_cache(zipcode: str, minYear: int, maxYear: int):
    pull_data(api_key, zipcode, minYear, maxYear)

@app.get("/load/zip/{zipcode}/years/{minYear}-{maxYear}/export")
async def export_csv(zipcode: str, minYear: int, maxYear: int):
    df, year_len = pull_data(api_key, zipcode, minYear, maxYear)
    print("df1: ", df)
    export_df = main.export_csv(df)
    print("df2: ", export_df)
    stream = io.StringIO()
    export_df.to_csv(stream, index=True)
    response = StreamingResponse(
        iter([stream.getvalue()]), media_type='text/csv')
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response

@app.get("/viz/zip/{zipcode}/years/{minYear}-{maxYear}/var/{variable}")
async def viz(zipcode: str, minYear: int, maxYear: int, variable: str):
    df, year_len = pull_data(api_key, zipcode, minYear, maxYear)
    plot_html = main.execute_viz(df, year_len, variable)
    return HTMLResponse(content=plot_html)

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 10000))
    #uvicorn.run("app:app", host="0.0.0.0", port=port)
    # Local testing
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)