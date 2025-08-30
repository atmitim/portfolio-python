import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.get(f"{BASE_URL}/")
assert response.status_code == 200
print("✅ Endpoint racine OK")

response = requests.post(
    f"{BASE_URL}/generate-report",
    json={"title": "Test", "start_date": "2025-08-01", "end_date": "2025-08-31"}
)
assert response.status_code == 200
print("✅ Endpoint génération de rapport OK")
