import pytest
import types
import sys
import os

# Ajouter le dossier parent pour importer main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import main

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    return TestClient(main.app)

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    import requests
    def fake_requests_get(*args, **kwargs):
        class FakeResp:
            status_code = 200
        return FakeResp()
    monkeypatch.setattr(requests, "get", fake_requests_get)

@pytest.fixture
def fake_driver(monkeypatch):
    class FakeDriver:
        title = "Fake Title"
        def get(self, url): pass
        def quit(self): pass
        def save_screenshot(self, path):
            with open(path, "wb") as f:
                f.write(b"\x89PNG\r\n\x1a\n")
            return True
        def find_element(self, *args, **kwargs):
            return types.SimpleNamespace(clear=lambda: None, send_keys=lambda x: None, click=lambda: None)
        def find_elements(self, *args, **kwargs):
            return []
    monkeypatch.setattr(main, "get_chrome_driver", lambda: FakeDriver())
    return FakeDriver()
