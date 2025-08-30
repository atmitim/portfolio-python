import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT", None)
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

def get_chrome_driver(headless: bool = HEADLESS) -> webdriver.Chrome:
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    if USER_AGENT:
        opts.add_argument(f"user-agent={USER_AGENT}")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")
    opts.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)
