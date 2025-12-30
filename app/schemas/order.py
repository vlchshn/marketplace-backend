from datetime import datetime
from pydantic import BaseModel

# Що юзер надсилає, щоб купити (тільки ID товару)
class OrderCreate(BaseModel):
    product_id: int

# Що ми віддаємо у відповідь (чек про покупку)
class OrderResponse(BaseModel):
    id: int
    status: str
    product_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True