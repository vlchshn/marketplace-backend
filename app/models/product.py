from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float)

    # Зв'язок з юзером (Foreign Key)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Зворотній зв'язок
    owner: Mapped["User"] = relationship(back_populates="products")