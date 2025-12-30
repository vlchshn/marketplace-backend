from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# Налаштування хешування
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# --- НОВА ЛОГІКА ДЛЯ ТОКЕНІВ ---

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Створює JWT токен з даними користувача"""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    # Додаємо час закінчення дії токена
    to_encode.update({"exp": expire})

    # Шифруємо (підписуємо) токен нашим секретним ключем
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt