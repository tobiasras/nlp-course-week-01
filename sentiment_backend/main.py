from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from afinn import Afinn

class TextInput(BaseModel):
    text: str

app = FastAPI()

afinn_en = Afinn(language="en")

@app.get("/")
async def root():
    return {"message": "app is running good:)"}

@app.post("/v1/sentiment")
def analyze_sentiment(payload: TextInput):
    score = afinn_en.score(payload.text)
    return {"score": score}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
