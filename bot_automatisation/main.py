from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI()

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/bot-status")
def bot_status():
    driver = get_chrome_driver()
    driver.get("https://www.google.com")
    title = driver.title
    driver.quit()
    return {"title": title}

@app.get("/google-search")
def google_search(q: str):
    driver = get_chrome_driver()
    driver.get(f"https://www.google.com/search?q={q}")
    title = driver.title
    driver.quit()
    return {"title": title}

@app.post("/fill-form")
def fill_form():
    driver = get_chrome_driver()
    driver.get("https://www.example.com/form")
    # Exemple fictif
    element = driver.find_element("name", "username")
    element.send_keys("test_user")
    driver.quit()
    return {"status": "form filled"}

@app.get("/screenshot")
def screenshot():
    driver = get_chrome_driver()
    driver.get("https://www.example.com")
    path = "screenshot.png"
    driver.save_screenshot(path)
    driver.quit()
    return {"screenshot": path}
