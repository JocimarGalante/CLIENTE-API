from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Endereco(Base):
    __tablename__ = "enderecos"
    id = Column(Integer, primary_key=True, index=True)
    cep = Column(String, nullable=False)
    logradouro = Column(String)
    cidade = Column(String)
    numero = Column(String)
    complemento = Column(String)

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_cadastro = Column(String)
    endereco_id = Column(Integer, ForeignKey("enderecos.id"))
    endereco = relationship("Endereco")
    contatos = relationship("Contato", cascade="all, delete-orphan")

class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
