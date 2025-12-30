from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Імпортуємо наші інструменти
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash

# Створюємо ізольований роутер для користувачів
router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Реєстрація нового користувача:
    1. Перевіряємо, чи є вже такий email.
    2. Хешуємо пароль.
    3. Зберігаємо в базу.
    """
    # 1. Перевірка: чи існує вже такий email в базі?
    # Ми робимо SQL-запит: SELECT * FROM users WHERE email = ...
    query = select(User).where(User.email == user_data.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    # Якщо знайшли — викидаємо помилку 400 (Bad Request)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # 2. Створення нового користувача
    # Увага: ми не зберігаємо user_data.password напряму! Ми його хешуємо.
    new_user = User(
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password)
    )

    # 3. Додаємо в базу і зберігаємо
    db.add(new_user)
    await db.commit()
    # Оновлюємо об'єкт new_user, щоб отримати згенерований ID та дату створення
    await db.refresh(new_user)

    return new_user