from pydantic import BaseModel, Field


class ResumeSchema(BaseModel):
    content: str = Field(..., description="Content резюме.")
    score: float = Field(..., description="Score from Elasticsearch.")


class GigaChatAnswer(BaseModel):
    description: str
    resume: ResumeSchema


class Answer(BaseModel):
    gigachat_answer: GigaChatAnswer
    resumes: list[ResumeSchema]
