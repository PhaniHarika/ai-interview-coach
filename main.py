from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from interview_engine import generate_questions, get_feedback, get_final_summary
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
import os
if os.path.exists("static") and os.listdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

class RoleRequest(BaseModel):
    role: str
    num_questions: int = 5
    focus_areas: list[str] = ["Technical", "Behavioral"]

class FeedbackRequest(BaseModel):
    role: str
    question: str
    answer: str

class SummaryRequest(BaseModel):
    role: str
    qa_pairs: list[dict]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    ) 

@app.post("/generate-questions")
async def api_generate_questions(data: RoleRequest):
    full_role = f"{data.role} ({', '.join(data.focus_areas)})"
    questions = generate_questions(full_role, data.num_questions)
    return {"questions": questions}

@app.post("/get-feedback")
async def api_get_feedback(data: FeedbackRequest):
    feedback = get_feedback(data.role, data.question, data.answer)
    return {"feedback": feedback}

@app.post("/get-summary")
async def api_get_summary(data: SummaryRequest):
    pairs = [(p["question"], p["answer"]) for p in data.qa_pairs]
    summary = get_final_summary(data.role, pairs)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)