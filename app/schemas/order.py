from datetime import datetime
from pydantic import BaseModel


class OrderCreate(BaseModel):
    product_id: int


class OrderResponse(BaseModel):
    id: int
    status: str
    product_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
