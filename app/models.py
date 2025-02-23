from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Float)
    order_type = Column(String)
