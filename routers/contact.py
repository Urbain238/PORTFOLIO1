from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()

@router.get("/info")
def get_contact_info(db: Session = Depends(get_db)):
    return db.query(models.ContactInfo).first()

@router.post("/message", status_code=status.HTTP_201_CREATED)
def send_message(data: dict, db: Session = Depends(get_db)):
    msg = models.ContactMessage(**data)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return {"message": "Message envoyé avec succès"}

@router.get("/messages")
def get_all_messages(
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.ContactMessage).order_by(models.ContactMessage.created_at.desc()).all()
