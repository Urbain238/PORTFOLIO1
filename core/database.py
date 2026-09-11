from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings

# engine utilisant l'URL nettoyée et gérée par core/config.py
engine = create_engine(
    settings.sync_database_url,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dépendance permettant d'injecter la session DB dans les routeurs FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
