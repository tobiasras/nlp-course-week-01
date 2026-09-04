from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from afinn import Afinn

class TextInput(BaseModel):
    text: str

app = FastAPI()

afinn_en = Afinn(language="en")
afinn_da = Afinn(language="da")

@app.get("/")
async def root():
    return {"message": "app is running good:)"}

@app.post("/v1/sentiment")
def analyze_sentiment(payload: TextInput):
    score_en = afinn_en.score(payload.text)
    score_dk = afinn_da.score(payload.text)
    score = (score_dk + score_en) / 2
    return {"score": score}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
