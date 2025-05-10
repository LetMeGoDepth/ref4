from pydantic import BaseModel
from typing import Optional


class QueryParameters(BaseModel):
    text: Optional[str] = None 
    salary: Optional[int] = None
    per_page: Optional[int] = 100
    page: Optional[int] = 1

    
class Vacancy(BaseModel):
    company_name: str 
    experience: str 
    id: int
    name: str
    professional_roles: str 
    url: str
    vacancys_id: int
    vacancys_type: str 
    snippet_requirement: str 
    snippet_responsibility: str 
    salary: int
    