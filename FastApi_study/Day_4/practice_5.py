from pydantic import BaseModel, Field
import random
from datetime import datetime, timedelta

class OTPVerification(BaseModel):
    phone_number: str
    otp: int = Field(default_factory=lambda: random.randint(100000, 999999))  # 6자리 OTP 생성
    otp_expiry: str = Field(default_factory=lambda: (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S"))

# 테스트
otp1 = OTPVerification(phone_number="010-1234-5678")
print(otp1)

otp2 = OTPVerification(phone_number="010-5678-1234")
print(otp2)