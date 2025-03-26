from sqlalchemy import Column, Integer, String, Date
from src.db import Base

class Operadora(Base):
    __tablename__ = "operadoras_saude"

    registro_ans = Column(String, primary_key=True, index=True)
    cnpj = Column(String)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    modalidade = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    uf = Column(String)
    cep = Column(String)
    ddd = Column(String)
    telefone = Column(String)
    fax = Column(String)
    endereco_eletronico = Column(String)
    representante = Column(String)
    cargo_representante = Column(String)
    regiao_de_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)
