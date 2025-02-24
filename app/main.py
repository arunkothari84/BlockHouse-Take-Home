from fastapi import FastAPI

from app.database import db_close, db_init
from app.routers import orders


async def lifespan(app):
    print("startup: connecting to database")
    await db_init()
    yield
    print("shutdown: closing database connection")
    await db_close()

app = FastAPI(lifespan=lifespan)

app.include_router(orders.router)
