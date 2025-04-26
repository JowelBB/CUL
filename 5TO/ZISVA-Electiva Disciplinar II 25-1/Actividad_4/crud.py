from sqlalchemy.orm import Session
from models import Item

def get_all_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, name: str, description: str, price: int, categoria_id: int):
    db_item = Item(nombre=name, descripcion=description, precio=price, categoria_id=categoria_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, name: str = None, description: str = None, price: int = None, categoria_id: int = None):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        if name is not None:
            db_item.nombre = name
        if description is not None:
            db_item.descripcion = description
        if price is not None:
            db_item.precio = price
        if categoria_id is not None:
            db_item.categoria_id = categoria_id
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
