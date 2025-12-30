from datetime import datetime
from pydantic import BaseModel, EmailStr

# Базова частина (спільна для входу і виходу)
class UserBase(BaseModel):
    email: EmailStr

# Анкету для РЕЄСТРАЦІЇ (клієнт вводить пароль)
class UserCreate(UserBase):
    password: str

# Анкету для ВІДПОВІДІ (ми показуємо ID, але приховуємо пароль)
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        # Ця магія дозволяє Pydantic читати дані прямо з бази
        from_attributes = True