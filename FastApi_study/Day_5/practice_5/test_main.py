import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from database import Base, get_db, Product
from main import app

# 테스트용 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

# 한 번만 실행하여 전체 테스트에서 DB를 공유
@pytest.fixture(scope="module")
def setup_test_db():
    Base.metadata.create_all(bind=engine)  # 새로 생성
    db = TestingSessionLocal()

    # 초기 데이터 삽입
    test_product = Product(id=1, name="Laptop", price=1500)
    db.add(test_product)
    db.commit()
    
    yield db  # 모든 테스트에서 공유됨

    db.close()
    Base.metadata.drop_all(bind=engine)  # 모든 테스트 종료 후 DB 삭제

# 제품 추가 API 테스트
def test_create_product(setup_test_db):
    response = client.post("/products/", json={"name": "Phone", "price": 800})
    assert response.status_code == 200
    assert response.json()["name"] == "Phone"
    assert response.json()["price"] == 800

# 존재하는 제품 조회 테스트 (Laptop & Phone 조회 가능)
def test_read_product(setup_test_db):
    response = client.get("/products/1")  # ID=1 Laptop 조회
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 1500

    response = client.get("/products/2")  # ID=2 Phone 조회
    assert response.status_code == 200
    assert response.json()["name"] == "Phone"
    assert response.json()["price"] == 800

# 존재하지 않는 제품 조회 테스트 (404 반환)
def test_read_product_not_found(setup_test_db):
    response = client.get("/products/999")  # 존재하지 않는 ID 요청
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"