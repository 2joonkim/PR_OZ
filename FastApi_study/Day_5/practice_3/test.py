from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_divide_api():
    """FastAPI 엔드포인트에서 기본적인 나눗셈 연산 테스트"""
    response = client.get("/math/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_negative_api():
    """음수 나눗셈 테스트"""
    response = client.get("/math/divide", params={"a": -10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": -5.0}

def test_divide_mixed_negative_api():
    """양수 ÷ 음수 테스트"""
    response = client.get("/math/divide", params={"a": 10, "b": -2})
    assert response.status_code == 200
    assert response.json() == {"result": -5.0}

def test_divide_zero_numerator_api():
    """0을 나누는 경우 테스트 (0 ÷ b)"""
    response = client.get("/math/divide", params={"a": 0, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 0.0}

def test_divide_by_zero_api():
    """0으로 나누는 경우:  HTTP 400 예외 발생"""
    response = client.get("/math/divide", params={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}