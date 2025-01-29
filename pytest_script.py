import requests

def test_homepage():
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
    assert "Home Page" in response.text
