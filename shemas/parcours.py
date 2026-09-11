from pydantic import BaseModel, ConfigDict
from typing import Optional

class ParcoursBase(BaseModel):
    titre: str
    etablissement: Optional[str] = None
    periode: Optional[str] = None
    statut: str  # ex: "valide", "en_cours", "a_venir"
    description: Optional[str] = None
    ordre: int = 0

class ParcoursCreate(ParcoursBase):
    pass

class ParcoursResponse(ParcoursBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
