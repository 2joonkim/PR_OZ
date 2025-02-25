from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # UUID 자동 생성
    name: str
    role: str = "user"  # 기본값 설정
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ✅ 테스트
user1 = User(name="Alice")
print(user1)

user2 = User(name="Bob", role="admin")  # role 변경 가능
print(user2)