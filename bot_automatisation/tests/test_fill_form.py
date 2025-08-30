def test_fill_form(fake_driver, client):
    response = client.post("/fill-form")
    assert response.status_code == 200
    assert response.json()["status"] == "form filled"
