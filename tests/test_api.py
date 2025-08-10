import pytest
from fastapi.testclient import TestClient
from fastAPI.iris_api import app  # Adjust import path as per your project

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Iris prediction API" in response.json().get("message", "")

def test_predict():
    response = client.post(
        "/predict",
        data={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        },
    )
    assert response.status_code == 200
    assert "Iris" in response.text  # Should return prediction in HTML
