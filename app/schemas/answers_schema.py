from datetime import datetime
from pydantic import BaseModel, Field


class AnswerBase(BaseModel):
    text: str = Field(..., min_length=1)


class AnswerCreate(AnswerBase):
    user_id: str


class AnswerOut(AnswerBase):
    id: int
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True