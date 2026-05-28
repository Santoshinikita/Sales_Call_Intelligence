from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.mock_llm import generate_mock_analysis

app = FastAPI(title="Sales Call Intelligence")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None,
            "transcript": ""
        }
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    transcript: str = Form(...)
):

    result = generate_mock_analysis(transcript)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "transcript": transcript
        }
    )
