from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    description: str | None = None
    price: float

class ProductCreate(ProductBase):
    pass

# --- НОВИЙ КЛАС ---
class ProductUpdate(BaseModel):
    # Всі поля необов'язкові (None), щоб можна було оновити щось одне
    title: str | None = None
    description: str | None = None
    price: float | None = None
# ------------------

class ProductResponse(ProductBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True