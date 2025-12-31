from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.order import Order
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderCreate, OrderResponse
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
        order_data: OrderCreate,
        current_user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db),
):
    query = select(Product).where(Product.id == order_data.product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    new_order = Order(
        user_id=current_user.id, product_id=product.id, status="completed"
    )

    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return new_order


@router.get("/", response_model=list[OrderResponse])
async def read_my_orders(
        current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    query = select(Order).where(Order.user_id == current_user.id)
    result = await db.execute(query)
    return result.scalars().all()
