from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from schemas import QueryParameters
from database import Vacancy
from crud import create_vacancy
from crud import update_vacancy
from parser import get_vacancys


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/vacancys_filter')
def vacancys_filter(db: Session = Depends(get_db)):
    items = db.query(Vacancy).all()
    return items



@router.post('/vacancys_post')
def vacancys_post(params: QueryParameters, db: Session = Depends(get_db)):
    vacs = get_vacancys(params)
    db.query(Vacancy).delete()
    db.commit()
    for vac in vacs:
        vacancys_table = db.query(Vacancy).filter_by(vacancys_id=vac["vacancys_id"]).first()
        if vacancys_table is not None:
            update_vacancy(db, vac)
        else:
            create_vacancy(db, vac)
    return vacs
