from fastapi import FastAPI

from app.database import db_close, db_init
from app.routers import orders


# Define the lifespan function separately
async def lifespan(app):
    print("startup: connecting to database")
    await db_init()
    yield
    print("shutdown: closing database connection")
    await db_close()

# Create the FastAPI app and use the lifespan function
app = FastAPI(lifespan=lifespan)

# Include the orders router
app.include_router(orders.router)
