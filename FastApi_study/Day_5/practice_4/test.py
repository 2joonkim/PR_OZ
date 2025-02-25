from fastapi.testclient import TestClient
from main import app, get_fake_items_db

client = TestClient(app)

test_items_db = {
    1: {"id": 1, "name": "Test Laptop", "price": 1000},
    2: {"id": 2, "name": "Test Phone", "price": 700},
}

def override_get_fake_items_db():
    """테스트용 가짜 데이터베이스 반환"""
    return test_items_db

app.dependency_overrides[get_fake_items_db] = override_get_fake_items_db

def test_get_existing_item():
    """존재하는 아이템 조회 테스트"""
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Laptop", "price": 1000}

def test_get_another_existing_item():
    """또 다른 아이템 조회 테스트"""
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {"id": 2, "name": "Test Phone", "price": 700}

def test_get_non_existing_item():
    """존재하지 않는 아이템 조회 (404 에러)"""
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}