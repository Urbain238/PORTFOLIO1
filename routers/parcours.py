from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()


@router.get("/")
def get_all_parcours(db: Session = Depends(get_db)):
    return db.query(models.Parcours).order_by(models.Parcours.ordre.asc()).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_parcours(
    data: dict,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    item = models.Parcours(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{parcours_id}")
def update_parcours(
    parcours_id: int,
    data: dict,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    item = db.query(models.Parcours).filter(models.Parcours.id == parcours_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Élément introuvable")

    for key, value in data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{parcours_id}")
def delete_parcours(
    parcours_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    item = db.query(models.Parcours).filter(models.Parcours.id == parcours_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Élément introuvable")
    db.delete(item)
    db.commit()
    return {"message": "Étape de parcours supprimée"}
