from app import app

def test_calculate_bill():
    client = app.test_client()
    # Test case: 5 items at $20 each = $100
    response = client.post("/calculate", json={"price": 20, "quantity": 5})
    assert response.status_code == 200
    assert response.json["total_bill"] == 100

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200