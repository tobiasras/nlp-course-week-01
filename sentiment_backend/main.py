from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class TextInput(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "app is running good"}

@app.post("/v1/sentiment")
def analyze_sentiment(text: TextInput):
    print(text)
    return {"score": 0}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)