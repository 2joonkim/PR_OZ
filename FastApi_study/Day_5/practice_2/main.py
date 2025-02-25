from fastapi import FastAPI, Depends

app = FastAPI()

def get_multiplier():
    """기본 곱셈 값을 반환하는 의존성 함수"""
    return 2  # 기본 곱셈 값

def multiply(a: int, b: int, multiplier: int = Depends(get_multiplier)):
    """곱셈 연산 함수 (Depends 사용)"""
    return {"result": (a * b) * multiplier}

@app.get("/math/multiply")
async def multiply_endpoint(a: int, b: int, multiplier: int = Depends(get_multiplier)):
    """FastAPI 엔드포인트"""
    return multiply(a, b, multiplier)