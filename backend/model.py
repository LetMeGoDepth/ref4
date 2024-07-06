#import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Vacancie(Base):


    __tablename__ = "vacancies"


    id = Column(Integer, primary_key=True)
    vacancies_id = Column(Integer)
    url = Column(String)
    name = Column(String)
    company_name = Column(String)
    vacancies_type = Column(String)
    professional_roles = Column(String)
    snippet_requirement = Column(String)
    snippet_responsibility = Column(String)
    experience = Column(String)
    salary = Column(String)