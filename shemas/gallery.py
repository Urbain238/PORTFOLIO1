from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class GalleryItemBase(BaseModel):
    title: Optional[str] = None
    image_url: str
    description: Optional[str] = None

class GalleryItemCreate(GalleryItemBase):
    pass

class GalleryItemResponse(GalleryItemBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
