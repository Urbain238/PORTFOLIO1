from sqlalchemy import Column, Integer, String, Text
from core.database import Base

class Parcours(Base):
    __tablename__ = "parcours"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(150), nullable=False)
    etablissement = Column(String(150))
    periode = Column(String(50))
    statut = Column(String(50), nullable=False)
    description = Column(Text)
    ordre = Column(Integer, default=0)
