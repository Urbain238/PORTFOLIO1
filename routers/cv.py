from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()

@router.get("/")
def get_public_cv(db: Session = Depends(get_db)):
    cv = db.query(models.CurriculumVitae).filter(models.CurriculumVitae.is_public == True).first()
    if not cv:
        raise HTTPException(status_code=404, detail="Aucun CV public disponible")
    return cv

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_cv(
    data: dict, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    cv = models.CurriculumVitae(**data)
    db.add(cv)
    db.commit()
    db.refresh(cv)
    return cv
