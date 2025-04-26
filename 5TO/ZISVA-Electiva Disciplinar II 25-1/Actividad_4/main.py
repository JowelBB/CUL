from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import SessionLocal, engine
from models import Base, Item
from crud import get_item, create_item, get_all_items, update_item, delete_item

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

@app.get("/productos/")
async def get_all_items_endpoint(db: Session = Depends(get_db)):
    items = get_all_items(db)
    return items

@app.get("/productos/{item_id}")
async def get_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Product not fount")
    return item

@app.put("/productos/{item_id}")
async def update_item_endpoint(item_id: int, nombre: str = None, descripcion: str = None, precio: int = None, categoria_id: int = None, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, nombre, descripcion, precio, categoria_id)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_item

@app.delete("/productos/{item_id}")
async def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    if delete_item(db, item_id):
        return {"detail": "Producto eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Product not fount")

