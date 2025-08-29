from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models import Question, Answer
from app.schemas import QuestionCreate, QuestionOut, AnswerCreate, AnswerOut
from app.core.logger import logger

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=QuestionOut, status_code=201)
def create_question(data: QuestionCreate, db: Session = Depends(get_db)):
    q = Question(text=data.text)
    db.add(q)
    db.commit()
    db.refresh(q)
    logger.info(f"Question created: id={q.id}, text='{q.text}'")
    return q

@router.get("/", response_model=list[QuestionOut])
def list_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).all()
    logger.info(f"Fetched {len(questions)} questions")
    return questions

@router.get("/{id}", response_model=QuestionOut)
def get_question(id: int, db: Session = Depends(get_db)):
    q = db.query(Question).get(id)
    if not q:
        logger.warning(f"Tried to fetch non-existent question id={id}")
        raise HTTPException(404, detail="Question not found")
    logger.info(f"Fetched question id={id} with {len(q.answers)} answers")
    return q

@router.delete("/{id}", status_code=204)
def delete_question(id: int, db: Session = Depends(get_db)):
    q = db.query(Question).get(id)
    if not q:
        logger.warning(f"Tried to delete non-existent question id={id}")
        raise HTTPException(404, detail="Question not found")
    db.delete(q)
    db.commit()
    logger.info(f"Question deleted: id={id}")
    return None

@router.post("/{id}/answers/", response_model=AnswerOut, status_code=201)
def add_answer(id: int, data: AnswerCreate, db: Session = Depends(get_db)):
    q = db.query(Question).get(id)
    if not q:
        logger.warning(f"Tried to add answer to non-existent question id={id}")
        raise HTTPException(404, detail="Question not found")

    ans = Answer(question_id=id, user_id=data.user_id, text=data.text)
    db.add(ans)
    db.commit()
    db.refresh(ans)
    logger.info(f"Answer created: id={ans.id} for question_id={id} by user={data.user_id}")
    return ans