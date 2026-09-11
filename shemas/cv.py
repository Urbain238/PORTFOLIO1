from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime

# Sub-schemas
class CVExperienceBase(BaseModel):
    job_title: str
    company_name: str
    start_date: str
    end_date: Optional[str] = None
    description: Optional[str] = None

class CVExperienceResponse(CVExperienceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CVEducationBase(BaseModel):
    degree: str
    institution: str
    year: str

class CVEducationResponse(CVEducationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CVSkillBase(BaseModel):
    name: str

class CVSkillResponse(CVSkillBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CVLanguageBase(BaseModel):
    language: str
    level: str

class CVLanguageResponse(CVLanguageBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Main CV schema
class CVBase(BaseModel):
    photo_url: Optional[str] = None
    first_name: str
    last_name: str
    target_title: str
    email: EmailStr
    phone: Optional[str] = None
    location: Optional[str] = None
    about_me: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    website_url: Optional[str] = None
    is_public: bool = True
    status: str = "published"

class CVCreate(CVBase):
    experiences: List[CVExperienceBase] = []
    educations: List[CVEducationBase] = []
    skills: List[CVSkillBase] = []
    languages: List[CVLanguageBase] = []

class CVResponse(CVBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    experiences: List[CVExperienceResponse] = []
    educations: List[CVEducationResponse] = []
    skills: List[CVSkillResponse] = []
    languages: List[CVLanguageResponse] = []

    model_config = ConfigDict(from_attributes=True)
