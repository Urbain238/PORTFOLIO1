from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

import models
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

# Synchronisation et création automatique des tables dans PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuration CORS pour autoriser le Frontend (Netlify / Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre avec votre URL Netlify en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enregistrement des endpoints séparés par module
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
    return {"status": "API Portfolio opérationnelle", "version": "1.0.0"}


# Adaptateur Serverless pour le déploiement sur Vercel
handler = Mangum(app)
