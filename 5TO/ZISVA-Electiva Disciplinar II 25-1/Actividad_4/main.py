from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import SessionLocal, engine
from models import Base, Item
from crud import get_item, create_item

app = FastAPI()

#Create tables in the databse
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/productos/")
async def get_item_endpoint(nombre: str, descripcion: str, precio: int, categoria_id: int, db: Session = Depends(get_db)):
    return create_item(db, nombre, descripcion, precio, categoria_id)

@app.get("/productos/{item_id}")
async def get_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not fount")
    return item