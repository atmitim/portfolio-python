def test_bot_status(fake_driver, client):
    response = client.get("/bot-status")
    assert response.status_code == 200
    assert response.json()["title"] == "Fake Title"
