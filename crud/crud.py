from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from services.viacep_service import buscar_endereco_por_cep

def criar_cliente(db: Session, cliente: schemas.ClienteCreate):
    endereco_info = buscar_endereco_por_cep(cliente.endereco.cep)
    endereco = models.Endereco(
        cep=cliente.endereco.cep,
        logradouro=endereco_info["logradouro"],
        cidade=endereco_info["cidade"],
        numero=cliente.endereco.numero,
        complemento=cliente.endereco.complemento
    )
    db.add(endereco)
    db.commit()
    db.refresh(endereco)

    db_cliente = models.Cliente(
        nome=cliente.nome,
        data_cadastro=cliente.data_cadastro,
        endereco_id=endereco.id
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)

    for c in cliente.contatos:
        contato = models.Contato(tipo=c.tipo, texto=c.texto, cliente_id=db_cliente.id)
        db.add(contato)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def listar_clientes(db: Session):
    return db.query(models.Cliente).all()

def obter_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def deletar_cliente(db: Session, cliente_id: int):
    cliente = obter_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente
