from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str
    title: Optional[str] = None
    hero_tagline: Optional[str] = None
    about_text: Optional[str] = None
    avatar_url: Optional[str] = None
    cv_pdf_url: Optional[str] = None
    is_available_for_work: bool = True

class ProfileCreate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
