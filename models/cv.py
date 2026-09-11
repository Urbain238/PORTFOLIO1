from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base

class CurriculumVitae(Base):
    __tablename__ = "curriculum_vitae"

    id = Column(Integer, primary_key=True, index=True)
    photo_url = Column(String(500), nullable=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    target_title = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(50), nullable=True)
    location = Column(String(150), nullable=True)
    about_me = Column(Text, nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    github_url = Column(String(255), nullable=True)
    website_url = Column(String(255), nullable=True)
    is_public = Column(Boolean, default=True)
    status = Column(String(50), default="published")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    experiences = relationship("CVExperience", back_populates="cv", cascade="all, delete-orphan")
    educations = relationship("CVEducation", back_populates="cv", cascade="all, delete-orphan")
    skills = relationship("CVSkill", back_populates="cv", cascade="all, delete-orphan")
    languages = relationship("CVLanguage", back_populates="cv", cascade="all, delete-orphan")


class CVExperience(Base):
    __tablename__ = "cv_experiences"

    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("curriculum_vitae.id"), nullable=False)
    job_title = Column(String(150), nullable=False)
    company_name = Column(String(150), nullable=False)
    start_date = Column(String(50), nullable=False)
    end_date = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)

    cv = relationship("CurriculumVitae", back_populates="experiences")


class CVEducation(Base):
    __tablename__ = "cv_educations"

    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("curriculum_vitae.id"), nullable=False)
    degree = Column(String(150), nullable=False)
    institution = Column(String(150), nullable=False)
    year = Column(String(50), nullable=False)

    cv = relationship("CurriculumVitae", back_populates="educations")


class CVSkill(Base):
    __tablename__ = "cv_skills"

    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("curriculum_vitae.id"), nullable=False)
    name = Column(String(100), nullable=False)

    cv = relationship("CurriculumVitae", back_populates="skills")


class CVLanguage(Base):
    __tablename__ = "cv_languages"

    id = Column(Integer, primary_key=True, index=True)
    cv_id = Column(Integer, ForeignKey("curriculum_vitae.id"), nullable=False)
    language = Column(String(100), nullable=False)
    level = Column(String(10), nullable=False)

    cv = relationship("CurriculumVitae", back_populates="languages")
