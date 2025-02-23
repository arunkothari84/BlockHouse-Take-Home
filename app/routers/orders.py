from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import SessionLocal
from app.models import Order, OrderCreate

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/orders/")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    new_order = Order(**order.dict())
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    # Notify WebSocket clients about the new order
    await manager.broadcast(f"New order created: {new_order.symbol} - {new_order.quantity} @ {new_order.price}")

    return new_order


@router.get("/orders/")
async def read_orders(db: AsyncSession = Depends(get_db)):
    stmt = select(Order)
    results = await db.execute(stmt)
    return results.scalars().all()


# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(data)
            except WebSocketDisconnect:
                self.disconnect(connection)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Received from client: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
