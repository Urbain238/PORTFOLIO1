from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class ProjectImageBase(BaseModel):
    image_url: str
    caption: Optional[str] = None

class ProjectImageResponse(ProjectImageBase):
    id: int
    project_id: int

    model_config = ConfigDict(from_attributes=True)

class ProjectBase(BaseModel):
    title: str
    short_description: Optional[str] = None
    full_description: Optional[str] = None
    cover_image: Optional[str] = None
    demo_url: Optional[str] = None
    github_url: Optional[str] = None
    technologies: Optional[List[str]] = []
    is_featured: bool = False

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime
    images: List[ProjectImageResponse] = []

    model_config = ConfigDict(from_attributes=True)
