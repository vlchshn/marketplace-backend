from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.product import Product
from app.models.user import User
# Додали ProductUpdate в імпорти
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.api.deps import get_current_user

router = APIRouter()


# 1. СТВОРЕННЯ (CREATE)
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
        product_data: ProductCreate,
        current_user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    new_product = Product(
        title=product_data.title,
        description=product_data.description,
        price=product_data.price,
        owner_id=current_user.id
    )

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


# 2. ЧИТАННЯ СПИСКУ (READ LIST)
@router.get("/", response_model=list[ProductResponse])
async def read_products(
        skip: int = 0,
        limit: int = 10,
        db: AsyncSession = Depends(get_db)
):
    query = select(Product).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


# 3. ВИДАЛЕННЯ (DELETE)
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product_id: int,
        current_user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this product")

    await db.delete(product)
    await db.commit()


# 4. ОНОВЛЕННЯ (UPDATE) - НОВЕ
@router.patch("/{product_id}", response_model=ProductResponse)
async def update_product(
        product_id: int,
        product_update: ProductUpdate,
        current_user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    """
    Оновити товар (ціну, назву або опис).
    Тільки для власника.
    """
    # Шукаємо товар
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Перевіряємо права
    if product.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this product")

    # Оновлюємо поля (exclude_unset=True бере тільки ті поля, що змінилися)
    update_data = product_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(product, key, value)

    await db.commit()
    await db.refresh(product)

    return product