# 여러 필드 검증 : Pydantic 모델 사용
from pydantic import BaseModel, model_validator, ValidationError

class ContactInfo(BaseModel):
    email: str | None = None
    phone_number: str | None = None

    @model_validator(mode="before")
    @classmethod
    def preprocess_email(cls, data):
        if isinstance(data, dict) and "email" in data and data["email"]:
            data["email"] = data["email"].lower()
        return data

    @model_validator(mode="after")
    def check_contact_info(self):
        if not self.email and not self.phone_number:
            raise ValidationError("Either email or phone_number must be provided")
        return self


try:
    contact = ContactInfo(email="Hello@example.com", phone_number="01011112222")
except ValidationError as e:
    print(e)