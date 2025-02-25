from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# 데이터베이스 대신 사용할 가짜 데이터 (딕셔너리 형태)
fake_items_db = {
    1: {"id": 1, "name": "Laptop", "price": 1200},
    2: {"id": 2, "name": "Phone", "price": 800},
    3: {"id": 3, "name": "Tablet", "price": 600},
}

def get_fake_items_db():
    """가짜 데이터베이스 반환 (의존성 주입)"""
    return fake_items_db

@app.get("/items/{item_id}")
def get_item(item_id: int, db: dict = Depends(get_fake_items_db)):
    item = db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item