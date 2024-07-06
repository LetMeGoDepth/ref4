import sqlalchemy as sq
from sqlalchemy.orm import Session
from cls import ParsVs
from cls import Paransies
from model import Vacancie




def cr_vac(db: Session, vacancies: ParsVs):
    db_vacs = Vacancie(**vacancies)
    db.add(db_vacs)
    db.commit()
    return db_vacs




def upd_vac(db: Session, vacancies: dict):
    db_vacs = db.query(Vacancie).filter(Vacancie == vacancies['vacancies_id'])
    for var, value in vacancies.items():
        setattr(db_vacs, var, value) if value else None
    db.commit()
    return db_vacs
