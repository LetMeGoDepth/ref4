from pydantic import BaseModel
from typing import Optional


class Paransies(BaseModel):
    text: Optional[str] = None 
    salary: Optional[int] = None
    per_page: Optional[int] = 100
    page: Optional[int] = 1

    


class ParsVs(BaseModel):
    company_name: str 
    experience: str 
    id: int
    name: str
    professional_roles: str 
    url: str
    vacancies_id: int
    vacancies_type: str 
    snippet_requirement: str 
    snippet_responsibility: str 
    salary: str
    