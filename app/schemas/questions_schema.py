from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.schemas.answers_schema import AnswerOut


class QuestionBase(BaseModel):
    text: str = Field(..., min_length=1)


class QuestionCreate(QuestionBase):
    pass


class QuestionOut(QuestionBase):
    id: int
    created_at: datetime
    answers: List[AnswerOut] = []

    class Config:
        from_attributes = True
