from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import src.models
from src.posts.operadora_service import get_operadora
from src.schema_operadora import OperadoraSchema
from src.db import SessionLocal, engine
from typing import List

src.models.Base.metadata.create_all(bind=engine)
route_operadora = APIRouter()

def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@route_operadora.get('/operadora/', response_model=List[OperadoraSchema], status_code=200)
def get_operadoraf(database: Session = Depends(get_db), query: str = ''):
    db_operadora = get_operadora(database, query)
    return db_operadora
