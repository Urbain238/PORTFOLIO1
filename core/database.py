import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Récupération de l'URL de base de données
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Supabase / Neon fournissent souvent une URL commençant par postgres://
# SQLAlchemy requiert obligatoirement le préfixe postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# pool_pre_ping=True évite les erreurs de connexion fermée courantes en serverless
engine = create_engine(
    DATABASE_URL,
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
