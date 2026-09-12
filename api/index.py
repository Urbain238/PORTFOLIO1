from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

import models
from core.config import settings
from core.database import engine
from routers import (
    auth,
    contact,
    cv,
    gallery,
    parcours,
    profile,
    project,
    secrets,
)

# Synchronisation sécurisée contre les interruptions de connexion serverless
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Connexion DB établie / Tables déjà existantes: {e}")

project_title = getattr(settings, "PROJECT_NAME", None) or "Portfolio API"
project_version = getattr(settings, "VERSION", None) or "1.0.0"
allowed_origins = getattr(settings, "ALLOWED_ORIGINS", None) or ["*"]

app = FastAPI(
    title=project_title,
    version=project_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Autorisation CORS complète pour éviter le blocage Preflight OPTIONS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enregistrement des routeurs
app.include_router(auth.router, prefix="/api/auth", tags=["Authentification"])
app.include_router(profile.router, prefix="/api/profile", tags=["Profil"])
app.include_router(parcours.router, prefix="/api/parcours", tags=["Parcours"])
app.include_router(project.router, prefix="/api/projects", tags=["Projets"])
app.include_router(gallery.router, prefix="/api/gallery", tags=["Galerie"])
app.include_router(cv.router, prefix="/api/cv", tags=["Curriculum Vitae"])
app.include_router(contact.router, prefix="/api/contact", tags=["Contact"])
app.include_router(secrets.router, prefix="/api/secrets", tags=["Coffre-Fort"])


@app.get("/", tags=["Healthcheck"])
def read_root():
    return {
        "status": "API Portfolio opérationnelle",
        "version": project_version,
    }


handler = Mangum(app)
