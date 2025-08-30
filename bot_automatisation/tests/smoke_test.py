def test_bot_status(fake_driver, client):
    response = client.get("/bot-status")
    assert response.status_code == 200

def test_screenshot(fake_driver, client, tmp_path):
    response = client.get("/screenshot")
    assert response.status_code == 200

def test_fill_form(fake_driver, client):
    response = client.post("/fill-form")
    assert response.status_code == 200
