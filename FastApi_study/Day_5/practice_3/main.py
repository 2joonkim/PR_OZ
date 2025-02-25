from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/math/divide")
def divide(a: float, b: float):
    """두 숫자를 나누는 API (0으로 나누는 경우 예외 처리 포함)"""
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}