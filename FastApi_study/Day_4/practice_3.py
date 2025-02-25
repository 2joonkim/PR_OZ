# Pydantic 검증: 자동계산필드
from pydantic import BaseModel, field_validator, computed_field

class Order(BaseModel):
    name: str
    price: float
    discount: float = 0

    @field_validator("discount")
    @classmethod
    def validate_discount(cls, value):
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0 and 100")
        return value

    @computed_field  # 자동 계산 필드
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount / 100), 2)

try:
    product1 = Order(name="Laptop", price=1000, discount=10)
    print(product1.final_price)  # 900.0 (10% 할인 적용)

    product2 = Order(name="Smartphone", price=500)  # 할인율 기본값 0%
    print(product2.final_price)  # 500.0 (할인 없음)

    product3 = Order(name="Tablet", price=300, discount=120)
    
except ValueError as e:
    print("Error:", e)  # Discount must be between 0 and 100
