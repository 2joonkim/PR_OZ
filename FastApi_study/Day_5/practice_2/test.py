from main import multiply

def mock_get_multiplier():
    return 3

def test_multiply():
    """기본적인 곱셈 연산 테스트"""
    assert multiply(2, 3, multiplier=mock_get_multiplier()) == {"result": 18}  # (2 * 3) * 3

def test_multiply_negative():
    """음수 값을 포함한 곱셈 테스트"""
    assert multiply(-2, 4, multiplier=mock_get_multiplier()) == {"result": -24}  # (-2 * 4) * 3

def test_multiply_zero():
    """0을 포함한 곱셈 테스트"""
    assert multiply(0, 5, multiplier=mock_get_multiplier()) == {"result": 0}  # (0 * 5) * 3

def test_multiply_mocked_multiplier():
    """Mock된 multiplier 값을 사용하는 경우"""
    assert multiply(10, 2, multiplier=mock_get_multiplier()) == {"result": 60}  # (10 * 2) * 3