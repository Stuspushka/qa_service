from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models import Answer
from app.schemas import AnswerOut
from app.core.logger import logger

router = APIRouter(prefix="/answers", tags=["Answers"])

@router.get("/{id}", response_model=AnswerOut)
def get_answer(id: int, db: Session = Depends(get_db)):
    ans = db.query(Answer).get(id)
    if not ans:
        logger.warning(f"Tried to fetch non-existent answer id={id}")
        raise HTTPException(404, detail="Answer not found")
    logger.info(f"Fetched answer id={id} for question_id={ans.question_id}")
    return ans

@router.delete("/{id}", status_code=204)
def delete_answer(id: int, db: Session = Depends(get_db)):
    ans = db.query(Answer).get(id)
    if not ans:
        logger.warning(f"Tried to delete non-existent answer id={id}")
        raise HTTPException(404, detail="Answer not found")
    db.delete(ans)
    db.commit()
    logger.info(f"Answer deleted: id={id} for question_id={ans.question_id}")
    return None