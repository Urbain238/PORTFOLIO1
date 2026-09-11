from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from core.database import Base

class ContactInfo(Base):
    __tablename__ = "contact_info"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    phone = Column(String(50))
    location = Column(String(100))
    linkedin_url = Column(String(255))
    github_url = Column(String(255))
    twitter_url = Column(String(255))


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String(100), nullable=False)
    sender_email = Column(String(100), nullable=False)
    subject = Column(String(200))
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
