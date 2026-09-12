from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()

class ParcoursSchema(BaseModel):
    titre: str
    etablissement: Optional[str] = None
    annee: str
    description: Optional[str] = None
    en_cours: bool = False
    ordre: int = 0

@router.get("/")
def get_parcours(db: Session = Depends(get_db)):
    return db.query(models.Parcours).order_by(models.Parcours.ordre.asc()).all()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_parcours(
    data: ParcoursSchema, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    step = models.Parcours(**data.model_dump())
    db.add(step)
    db.commit()
    db.refresh(step)
    return step

@router.put("/{parcours_id}")
def update_parcours(
    parcours_id: int,
    data: ParcoursSchema,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    step = db.query(models.Parcours).filter(models.Parcours.id == parcours_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Étape non trouvée")
    
    for key, value in data.model_dump().items():
        setattr(step, key, value)
        
    db.commit()
    db.refresh(step)
    return step

@router.delete("/{parcours_id}")
def delete_parcours(
    parcours_id: int, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    step = db.query(models.Parcours).filter(models.Parcours.id == parcours_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Étape non trouvée")
    db.delete(step)
    db.commit()
    return {"message": "Étape supprimée"}
