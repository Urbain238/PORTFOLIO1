from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime

class SecretVaultBase(BaseModel):
    title: str
    category: str = "Général"
    item_type: str  # "text", "image", "audio", "video", "document"
    text_content: Optional[str] = None
    media_url: Optional[str] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size_bytes: Optional[int] = None
    extra_metadata: Optional[Dict[str, Any]] = None

class SecretVaultCreate(SecretVaultBase):
    pass

class SecretVaultResponse(SecretVaultBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
