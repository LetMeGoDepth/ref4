from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy as sq
from parcer import get_vacancies
from model import Base
from model import Vacancie
from crud import cr_vac
from crud import upd_vac
from cls import Paransies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


engine = create_engine('sqlite:///your_database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/vacancies_filter')
def vacancies_filter(db: Session = Depends(get_db)):
    items = db.query(Vacancie).all()
    return items





@app.post('/vacancies_post')
def vacancies_post(params: Paransies, db: Session = Depends(get_db)):
    Vacs = get_vacancies(params)
    db.query(Vacancie).delete()
    db.commit()
    for vac in Vacs:
        vacancies_table = db.query(Vacancie).filter_by(vacancies_id=vac["vacancies_id"]).first()
        if vacancies_table is not None:
            upd_vac(db, vac)
        else:
            cr_vac(db, vac)
    return Vacs





origins = [
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)