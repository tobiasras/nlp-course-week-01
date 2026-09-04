# NLP / LLMOps / Knowledge Graphs — Week 01

This repository is from the course **Natural language processing, large language model operations and knowledge graphs**, week 01.

The assignment is a bilingual (English and Danish) sentiment analysis service for short DTU course evaluations. On the dataset included in the demo UI, the service reached **70% accuracy**.

## What is in this repo

| Path | Description |
| --- | --- |
| `sentiment_backend/` | FastAPI service that scores text with [AFINN](https://github.com/fnielsen/afinn) (English and Danish lexicons). |
| `ui/` | Demo frontend for scoring a single text, running the labeled dataset, and showing accuracy and latency. |
| `test/sentiment_backend/` | Basic API tests for positive and negative examples. |
| `docker-compose.yml` | Runs the API and UI together. |

The API contract is:

- **POST** `/v1/sentiment`
- Request: `{"text": "<course evaluation>"}`
- Response: `{"score": <number>}`

The backend averages the English and Danish AFINN scores. The UI maps scores to labels with: ≤ −1 negative, between −1 and 1 neutral, ≥ 1 positive.

## How to run

### Docker (recommended)

From the project root:

```bash
docker compose up --build
```

Then open:

- UI: http://localhost:8001
- API: http://localhost:8000
- API docs: http://localhost:8000/docs

Stop with `Ctrl+C`, or `docker compose down`.

### Tests

With the backend dependencies installed:

```bash
pip install -r sentiment_backend/requirements.txt
python test/sentiment_backend/test_main.py
```

### Run without Docker

API:

```bash
pip install -r sentiment_backend/requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir sentiment_backend
```

UI (in another terminal):

```bash
pip install -r ui/requirements.txt
uvicorn sentiment_analysis_ui:app --reload --host 0.0.0.0 --port 8001 --app-dir ui
```

Point the UI “External service base URL” at `http://localhost:8000`.

