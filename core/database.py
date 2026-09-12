import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from core.config import settings

db_url = str(settings.sync_database_url)

# Correction du préfixe d'URL pour SQLAlchemy 2.0+
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

is_sqlite = "sqlite" in db_url

# Force le mode SSL obligatoire pour Neon PostgreSQL
if not is_sqlite and "sslmode" not in db_url:
    separator = "&" if "?" in db_url else "?"
    db_url = f"{db_url}{separator}sslmode=require"

connect_args = {"check_same_thread": False} if is_sqlite else {}

engine_kwargs = {
    "connect_args": connect_args,
    "pool_pre_ping": True,
}

if not is_sqlite:
    # NullPool évite l'épuisement des connexions sur Neon en environnement Serverless
    engine_kwargs["poolclass"] = NullPool

engine = create_engine(db_url, **engine_kwargs)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dépendance permettant d'injecter la session DB dans les routeurs FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
