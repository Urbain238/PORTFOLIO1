import os
from typing import List
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API & App Métadonnées
    PROJECT_NAME: str = "Portfolio API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"

    # Base de données (PostgreSQL - Neon / Supabase)
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/portfolio_db"

    @property
    def sync_database_url(self) -> str:
        """Convertit automatiquement le préfixe postgres:// fourni par Vercel/Supabase en postgresql://"""
        if self.DATABASE_URL and self.DATABASE_URL.startswith("postgres://"):
            return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)
        return self.DATABASE_URL

    # Sécurité & JWT
    SECRET_KEY: str = "SUPER_SECRET_KEY_A_CHANGER_EN_PRODUCTION_123456789"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 jours

    # CORS (Origines autorisées)
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://*.netlify.app",
        "https://*.vercel.app",
    ]

    @field_validator("ALGORITHM", mode="before")
    @classmethod
    def clean_algorithm(cls, v: str) -> str:
        if not v or not str(v).strip():
            return "HS256"
        return str(v).strip().strip('"').strip("'")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True
    )


# Instance globale réutilisable dans l'application
settings = Settings()
