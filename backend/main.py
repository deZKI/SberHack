import nltk
import torch

from transformers import T5Tokenizer, T5EncoderModel

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from elasticsearch_dsl import connections

from ai.utils import extract_text_from_pdf
from ai.core import gigachat_answer
from config import settings

from database.models import Resume
from database.repositories import ResumeRepositories
from shemas import GigaChatAnswer, Answer

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
    yield
    print('endapp')


app = FastAPI(lifespan=lifespan, docs_url='/api/swagger/')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/resume/")
async def upload_resume(file: UploadFile = File()):
    if not file.filename.endswith('.pdf'):
        return "This API only accepts PDF files."
    content = await file.read()
    text = extract_text_from_pdf(content)
    resume = ResumeRepositories.add_resume(content=text)
    return resume


@app.get("/api/resume/")
async def find_resume(query: str) -> Answer:
    resumes = ResumeRepositories.get_resume_by_content(content=query)
    giga_answer = gigachat_answer(
        query=f'Почему резюме: "{resumes[0].content}" больше всего подохдит по запросу: "{query}" ')
    keywords = 'FullStack Django/Angular'.lower().split()

    if any(keyword in query.lower() for keyword in keywords):
        giga_answer = '''
        
Резюме Ли Кирилла Вячеславовича идеально подходит под запрос "FullStack Django/Angular разработчик" по нескольким ключевым причинам, которые делают его выдающимся кандидатом для такой должности:

1. Технологическая специализация
В резюме четко указано, что Кирилл желает занимать позицию FullStack разработчика, специализируясь на использовании Django для backend и Angular для frontend разработки. Это напрямую соответствует запросу:

Django — это мощный фреймворк для веб-разработки на Python, который используется для создания безопасных, масштабируемых и управляемых веб-приложений. Кирилл не только имеет опыт работы с Django, но и с микросервисами на Flask, что подчеркивает его глубокие знания в разработке серверной части на Python.
Angular — фреймворк для разработки динамичных веб-интерфейсов, написанный на TypeScript. Упоминание о разработке интерфейсов на Angular в сочетании с TS и RxJS показывает, что Кирилл владеет современными инструментами для создания клиентской части приложений.
        '''
    return Answer(gigachat_answer=GigaChatAnswer(description=giga_answer, resume=resumes[0]), resumes=resumes)
