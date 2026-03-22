from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.spam import check_spam
app = FastAPI(title="SpamCheck Web")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/classify")
async def classify(request: Request):
    payload = await request.json()
    text = payload["text"]
    label, score = check_spam(text)
    return {
        "label": label, "score": score
    }