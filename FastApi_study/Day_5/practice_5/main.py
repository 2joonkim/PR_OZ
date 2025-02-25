from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db, Product

app = FastAPI()

# 요청 데이터 모델 정의
class ProductCreate(BaseModel):
    name: str
    price: int

# 제품 추가 API
@app.post("/products/")
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = Product(name=product.name, price=product.price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# 제품 조회 API
@app.get("/products/{product_id}")
async def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product