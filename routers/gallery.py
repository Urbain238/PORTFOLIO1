from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
import models

router = APIRouter()

@router.get("/")
def get_gallery_items(db: Session = Depends(get_db)):
    return db.query(models.GalleryItem).order_by(models.GalleryItem.created_at.desc()).all()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_gallery_item(
    data: dict, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    item = models.GalleryItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_gallery_item(
    item_id: int, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    item = db.query(models.GalleryItem).filter(models.GalleryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Image non trouvée")
    db.delete(item)
    db.commit()
    return {"message": "Image supprimée de la galerie"}
