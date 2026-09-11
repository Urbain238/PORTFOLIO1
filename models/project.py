from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    short_description = Column(String(255))
    full_description = Column(Text)
    cover_image = Column(String(500))
    demo_url = Column(String(500))
    github_url = Column(String(500))
    technologies = Column(JSON)
    is_featured = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    images = relationship("ProjectImage", back_populates="project", cascade="all, delete-orphan")


class ProjectImage(Base):
    __tablename__ = "project_images"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    image_url = Column(String(500), nullable=False)
    caption = Column(String(150))

    project = relationship("Project", back_populates="images")
