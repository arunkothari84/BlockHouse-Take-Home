import datetime

from fastapi.testclient import TestClient

from app.main import app  # Ensure correct import of your FastAPI app

# Initialize the TestClient without the keyword argument
client = TestClient(app)


def test_create_order():
    current_timestamp = datetime.datetime.now()
    response = client.post(
        "/orders/",
        json={"id": int(current_timestamp.timestamp()), "symbol": "AAPL", "price": 150.75,
              "quantity": 10, "order_type": "buy"},
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
