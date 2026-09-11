from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from core.database import Base

class SecretVault(Base):
    __tablename__ = "secret_vault"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    category = Column(String(50), default="Général")
    item_type = Column(String(50), nullable=False)
    text_content = Column(Text, nullable=True)
    media_url = Column(String(500), nullable=True)
    file_name = Column(String(150), nullable=True)
    mime_type = Column(String(100), nullable=True)
    file_size_bytes = Column(Integer, nullable=True)
    extra_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
