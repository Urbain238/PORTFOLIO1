from sqlalchemy import Column, Integer, String, Text, Boolean
from core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    title = Column(String(150))
    hero_tagline = Column(Text)
    about_text = Column(Text)
    avatar_url = Column(String(500))
    cv_pdf_url = Column(String(500))
    is_available_for_work = Column(Boolean, default=True)
