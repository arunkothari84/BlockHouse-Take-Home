from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./orders.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def db_close():
    await engine.dispose()
