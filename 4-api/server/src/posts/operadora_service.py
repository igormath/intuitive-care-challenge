from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException, status
from src.models import Operadora

def get_operadora(database: Session, empresa_query: str):
    if not empresa_query:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Operadora não informada.')

    termos = empresa_query.upper().split('%20')

    filtros = [Operadora.razao_social.like(f'%{termo}%') for termo in termos]

    operadoras = database.query(Operadora).filter(and_(*filtros)).all()
    
    if not operadoras:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Operadora não encontrada.')
    return operadoras
