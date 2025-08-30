def test_google_search(fake_driver, client):
    response = client.get("/google-search?q=test")
    assert response.status_code == 200
    assert response.json()["title"] == "Fake Title"
