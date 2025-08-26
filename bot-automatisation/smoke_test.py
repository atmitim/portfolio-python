import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

print("✅ Bot Automatisation : Packages installés")

# Vérifier que requests fonctionne
try:
    response = requests.get("https://www.google.com")
    print("Requests fonctionne :", response.status_code == 200)
except Exception as e:
    print("Erreur Requests :", e)

# Vérifier Selenium
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    print("Selenium fonctionne : page Google ouverte")
    driver.quit()
except Exception as e:
    print("Erreur Selenium :", e)

# Vérifier que TARGET_URL existe dans .env
TARGET_URL = os.getenv("TARGET_URL", "https://example.com")
print("TARGET_URL :", TARGET_URL)
