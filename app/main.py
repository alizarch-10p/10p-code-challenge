from fastapi import FastAPI
from app.routers import documents, answer
from decouple import config
import logging

OPENAI_API_KEY = config('OPENAI_API_KEY')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(documents.router)
app.include_router(answer.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
