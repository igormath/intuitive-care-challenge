from pydantic import BaseModel
from typing import Optional

class OperadoraSchema(BaseModel):
    cnpj: Optional[str] = None
    razao_social: Optional[str] = None
    cep: Optional[str] = None
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    endereco_eletronico: Optional[str] = None

    class Config:
        from_attributes: True
