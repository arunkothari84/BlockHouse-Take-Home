from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Float)
    order_type = Column(String)


# Pydantic model to validate input when creating an order
class OrderCreate(BaseModel):
    id: int
    symbol: str
    price: float
    quantity: float
    order_type: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy models as dicts
