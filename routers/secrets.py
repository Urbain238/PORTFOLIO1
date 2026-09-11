from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()

@router.get("/")
def get_vault_items(
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.SecretVault).order_by(models.SecretVault.created_at.desc()).all()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_vault_item(
    data: dict, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    item = models.SecretVault(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_vault_item(
    item_id: int, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    item = db.query(models.SecretVault).filter(models.SecretVault.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Élément introuvable")
    db.delete(item)
    db.commit()
    return {"message": "Élément supprimé du coffre-fort"}
