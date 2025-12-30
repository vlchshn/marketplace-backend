from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.api.routers import users, auth, products, orders
from app.api.routers import users, auth, products

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up... Connecting to DB...")
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    yield
    print("🛑 Shutting down...")
    await engine.dispose()

app = FastAPI(
    title="HexaStore API",
    description="High-load E-commerce API built with FastAPI",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, tags=["Authentication"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)