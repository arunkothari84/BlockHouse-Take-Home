from fastapi import FastAPI

from app.database import db_close, db_init
from app.routers import orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    print("startup: connecting to database")
    await db_init()

@app.on_event("shutdown")
async def shutdown():
    print("shutdown: closing database connection")
    await db_close()

# Include the orders router
app.include_router(orders.router)
