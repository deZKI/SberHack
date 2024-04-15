import nltk
import torch

from transformers import T5Tokenizer, T5EncoderModel

from fastapi import FastAPI, UploadFile, File

from contextlib import asynccontextmanager

from elasticsearch_dsl import connections

from ai.core import find_top_matches
from ai.utils import extract_text_from_pdf
from config import settings

from database.models import Resume
from database.repositories import ResumeRepositories
from shemas import MatchResult

RUSSIAN_STOP_WORDS = []
TOKENIZER = None
MODEL = None
DEVICE = None


async def start_database():
    print('start_database')
    connections.create_connection(hosts=f"http://{settings.DB_HOST}:{settings.DB_PORT}")
    Resume.init()


async def start_ml():
    print('start_ml')
    nltk.download('stopwords')
    global RUSSIAN_STOP_WORDS, TOKENIZER, MODEL, DEVICE
    RUSSIAN_STOP_WORDS = nltk.corpus.stopwords.words('russian')

    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    TOKENIZER = T5Tokenizer.from_pretrained('t5-small')
    MODEL = T5EncoderModel.from_pretrained('t5-small')
    TOKENIZER.save_pretrained('ai/tokenizer')
    MODEL.save_pretrained('ai/model')

    MODEL.to(DEVICE)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('startapp')
    await start_database()
    await start_ml()
    yield
    print('endapp')


app = FastAPI(lifespan=lifespan, docs_url='/api/swagger/')


@app.post("/api/resume/")
async def upload_resume(file: UploadFile = File()):
    if not file.filename.endswith('.pdf'):
        return "This API only accepts PDF files."
    content = await file.read()
    text = extract_text_from_pdf(content)
    resume = ResumeRepositories.add_resume(content=text)
    return resume


@app.get("/api/resume/")
async def find_resume(query: str) -> MatchResult:
    texts = ResumeRepositories.get_all_resumes()
    top_matches, scores = find_top_matches(texts=texts, reference_text=query)
    return MatchResult(matches=top_matches, scores=scores)
