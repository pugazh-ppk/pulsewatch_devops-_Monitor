from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"PulseWatch" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_empty_url_submission():
    client = app.test_client()
    response = client.post("/", data={"url": ""})
    assert response.status_code == 200
    assert b"Please enter a website URL" in response.data
