from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import db_close, db_init
from app.routers import orders


@asynccontextmanager
async def lifecycle():
    print("startup: connecting to database")
    await db_init()
    try:
        yield
    finally:
        print("shutdown: closing database connection")
        await db_close()


app = FastAPI(lifecycle=lifecycle)

app.include_router(orders.router)
