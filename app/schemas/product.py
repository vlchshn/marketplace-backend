from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: str | None = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None


class ProductResponse(ProductBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
