from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# 1. Створюємо асинхронний двигун
# echo=True буде показувати SQL-запити в консолі (корисно для налагодження)
engine = create_async_engine(str(settings.DATABASE_URL), echo=True)

# 2. Створюємо фабрику сесій
# Кожен запит від користувача отримуватиме свою окрему сесію з базою
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

# 3. Функція-генератор для отримання сесії (Dependency Injection)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session