import os
import csv
import time
from pathlib import Path
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Charger les variables d'environnement
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

URL = os.getenv("TARGET_URL")
print("TARGET_URL =", URL)
if not URL:
    raise ValueError("La variable TARGET_URL n'est pas définie dans le fichier .env")


def fetch_all_job_listings(url, max_pages=50, max_empty_pages=2):
    jobs = []
    page = 1
    empty_pages = 0

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # supprimé pour voir le navigateur
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    while page <= max_pages:
        paginated_url = f"{url}&page={page}"
        print(f"→ Scraping page {page}: {paginated_url}")

        driver.get(paginated_url)
        time.sleep(2)  # attendre le rendu JS

        job_cards = driver.find_elements(By.CSS_SELECTOR, "article.job.clicky")
        if not job_cards:
            empty_pages += 1
            print(f"→ Page vide détectée ({empty_pages}/{max_empty_pages})")
            if empty_pages >= max_empty_pages:
                break
        else:
            empty_pages = 0
            print(f"→ {len(job_cards)} offres détectées sur cette page")

            for card in job_cards:
                try:
                    title_elem = card.find_element(By.CSS_SELECTOR, "h2 a")
                    company_elem = card.find_element(By.CSS_SELECTOR, "p.company")
                    location_elem = card.find_element(By.CSS_SELECTOR, "ul.location li")

                    jobs.append({
                        "title": title_elem.get_attribute("title").strip(),
                        "company": company_elem.text.strip() if company_elem else "N/A",
                        "location": location_elem.text.strip() if location_elem else "N/A",
                        "link": "https://www.optioncarriere.com" + title_elem.get_attribute("href"),
                    })
                except Exception:
                    continue

        page += 1
        time.sleep(2)
    print(f"→ Total des offres récupérées : {len(jobs)}")
    driver.quit()
    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "company", "location", "link"])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
    print(f"{len(jobs)} offres sauvegardées dans {filename}")


def main():
    print("Début du scraping des offres d'emploi...")
    jobs = fetch_all_job_listings(URL)
    if jobs:
        save_to_csv(jobs)
    else:
        print("Aucune offre trouvée.")


if __name__ == "__main__":
    main()
