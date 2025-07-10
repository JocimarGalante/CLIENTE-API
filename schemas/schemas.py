from pydantic import BaseModel
from typing import List, Optional

class ContatoCreate(BaseModel):
    tipo: str
    texto: str

class Contato(ContatoCreate):
    id: int
    class Config:
        orm_mode = True

class EnderecoCreate(BaseModel):
    cep: str
    numero: str
    complemento: Optional[str] = None

class Endereco(BaseModel):
    cep: str
    logradouro: str
    cidade: str
    numero: str
    complemento: Optional[str] = None
    class Config:
        orm_mode = True

class ClienteCreate(BaseModel):
    nome: str
    data_cadastro: str
    endereco: EnderecoCreate
    contatos: List[ContatoCreate]

class Cliente(BaseModel):
    id: int
    nome: str
    data_cadastro: str
    endereco: Endereco
    contatos: List[Contato]
    class Config:
        orm_mode = True
