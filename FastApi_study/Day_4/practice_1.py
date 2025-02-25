from pydantic import BaseModel, field_validator, ValidationError
import re
import string

class User(BaseModel):
    username: str
    password: str 

@field_validator('password')
@classmethod
def validate_password(cls, password):
    if len(password) < 8:
        raise ValueError("패스워드는 8자 이상이어야 합니다.")
    if not re.search(r'[A-Z]', password):
        raise ValueError("패스워드는 최소 하나의 대문자가 포함되어야 합니다.")
    if not any(char in string.punctuation for char in password):
        raise ValueError("패스워드는 최소 하나의 특수문자가 포함되어야 합니다.")
    return password

try:
    user = User(username="testuser", password="Password123!")
    weak_user = User(username="weakuser", password="weakpass")
except ValidationError as e:
    print(e)
