from fastapi import FastAPI

app = FastAPI()

def add(a, b):
    """덧셈 연산 함수"""
    a, b = int(a), int(b)  # 숫자로 변환
    return {"result": a + b}

@app.get("/math/add")
async def add_endpoint(a: int, b: int):
    """FastAPI 엔드포인트"""
    return add(a, b)