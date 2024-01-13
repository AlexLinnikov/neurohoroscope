import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.post("/generate")
def read_root(request: Request):
    # TODO post method
    return templates.TemplateResponse(
        request=request, name="index.html")


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
