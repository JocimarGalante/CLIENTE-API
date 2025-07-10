from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import Base, engine, SessionLocal
from schemas import schemas
from crud import crud
import models.models as models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cliente API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.criar_cliente(db, cliente)

@app.get("/clientes", response_model=list[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.listar_clientes(db)

@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def obter_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.obter_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.delete("/clientes/{cliente_id}")
def excluir_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.deletar_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"ok": True}
