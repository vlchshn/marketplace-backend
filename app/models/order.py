from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Хто купує (User)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Що купує (Product)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    # Статус замовлення (pending, completed, canceled)
    status: Mapped[str] = mapped_column(String, default="pending")

    # Час покупки
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Зв'язки (щоб ми могли отримати об'єкти user і product через order.user / order.product)
    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship()