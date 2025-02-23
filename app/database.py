from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite (for example, you could also use PostgreSQL or MySQL)
DATABASE_URL = "sqlite+aiosqlite:///./order.db"

Base = declarative_base()

# Create an async engine for SQLAlchemy
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Use AsyncSession for async database operations
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Initialize the database by creating tables


async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Close the database connection


async def db_close():
    await engine.dispose()
