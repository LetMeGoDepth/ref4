from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///your_database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


class Vacancy(Base):


    __tablename__ = "Vacancy"


    id = Column(Integer, nullable=False, primary_key=True)
    vacancys_id = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    company_name = Column(String, nullable=True)
    vacancys_type = Column(String, nullable=True)
    professional_roles = Column(String, nullable=True)
    snippet_requirement = Column(String, nullable=False)
    snippet_responsibility = Column(String, nullable=False)
    experience = Column(String, nullable=True)
    salary = Column(Integer, nullable=True)
    