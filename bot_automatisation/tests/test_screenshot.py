def test_screenshot(fake_driver, client, tmp_path):
    response = client.get("/screenshot")
    path = tmp_path / "screenshot.png"
    with open(path, "wb") as f:
        f.write(b"dummy")
    assert response.status_code == 200
