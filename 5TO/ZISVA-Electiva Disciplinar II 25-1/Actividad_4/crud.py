from sqlalchemy.orm import Session
from models import Item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, name: str, description: str, price: int, categoria_id: int):
    db_item = Item(name=name, description=description, price=price, categoria_id=categoria_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item