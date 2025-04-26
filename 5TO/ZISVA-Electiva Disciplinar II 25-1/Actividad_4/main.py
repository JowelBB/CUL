from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import SessionLocal, engine
from models import Base, Products
from recursos.crud_productos import get_product, get_all_products, create_product, update_product, delete_product
from recursos.crud_categorias import get_category, get_all_categories, create_category, update_category, delete_category

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

# Rutes for products
@app.post("/productos/")
async def get_item_endpoint(name: str, description: str, price: int, categoria_id: int, db: Session = Depends(get_db)):
    return create_product(db, name, description, price, categoria_id)

@app.get("/productos/")
async def get_all_items_endpoint(db: Session = Depends(get_db)):
    products = get_all_products(db)
    return products

@app.get("/productos/{product_id}")
async def get_item_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/productos/{product_id}")
async def update_item_endpoint(product_id: int, name: str = None, description: str = None, price: int = None, categoria_id: int = None, db: Session = Depends(get_db)):
    updated_product = update_product(db, product_id, name, description, price, categoria_id)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@app.delete("/productos/{product_id}")
async def delete_item_endpoint(product_id: int, db: Session = Depends(get_db)):
    if delete_product(db, product_id):
        return {"detail": "Deleted product"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")

# Rutes for Categories
@app.post("/categorias/")
async def get_category_endpoint(name: str, db: Session = Depends(get_db)):
    return create_category(db, name)

@app.get("/categorias/")
async def get_all_categories_endpoint(db: Session = Depends(get_db)):
    categories = get_all_categories(db)
    return categories

@app.get("/categorias/{category_id}")
async def get_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.put("/categorias/{category_id}")
async def update_category_endpoint(category_id: int, name: str = None, db: Session = Depends(get_db)):
    updated_category = update_category(db, category_id, name)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@app.delete("/categorias/{category_id}")
async def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    if delete_category(db, category_id):
        return {"detail": "Deleted category"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")