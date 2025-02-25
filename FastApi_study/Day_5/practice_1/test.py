from main import add

def test_add():
    """기본 테스트: 정상적인 숫자 입력"""
    assert add(5, 3) == {"result": 8}
    assert add(10, 20) == {"result": 30}

def test_add_negative():
    """마이너스 값 포함 테스트"""
    assert add(-5, 3) == {"result": -2}
    assert add(-10, -20) == {"result": -30}

def test_add_zero():
    """0을 더하는 경우 테스트"""
    assert add(0, 5) == {"result": 5}
    assert add(10, 0) == {"result": 10}
    assert add(0, 0) == {"result": 0}