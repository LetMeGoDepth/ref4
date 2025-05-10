from sqlalchemy.orm import Session
from schemas import Vacancy
from database import Vacancy


def create_vacancy(db: Session, vacancys: dict):
    db_vacs = Vacancy(**vacancys)
    db.add(db_vacs)
    db.commit()
    return db_vacs



def update_vacancy(db: Session, vacancys: dict):
    db_vacs = db.query(Vacancy).filter(Vacancy == vacancys['vacancys_id'])
    for var, value in vacancys.items():
        setattr(db_vacs, var, value) if value else None
    db.commit()
    return db_vacs