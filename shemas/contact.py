from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class ContactInfoBase(BaseModel):
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    twitter_url: Optional[str] = None

class ContactInfoResponse(ContactInfoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ContactMessageCreate(BaseModel):
    sender_name: str
    sender_email: EmailStr
    subject: Optional[str] = None
    message: str

class ContactMessageResponse(ContactMessageCreate):
    id: int
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
