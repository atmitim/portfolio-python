## Bot Automatisation![Python](https://img.shields.io/badge/python-3.13-blue)

![Python](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.115-green)
![Selenium](https://img.shields.io/badge/selenium-automation-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest%20passed-success)
![Smoke Test](https://img.shields.io/badge/smoke%20test-verified-blueviolet)
![CI](https://github.com/atmitim/portfolio-python/actions/workflows/tests.yml/badge.svg)


Un projet d’automatisation web basé sur Selenium, conçu pour interagir avec des pages web, remplir des formulaires, effectuer des recherches et prendre des captures d’écran automatiquement.

Il inclut une API légère avec FastAPI et un ensemble de tests automatisés avec pytest pour garantir la fiabilité.

🚀 Fonctionnalités principales

Lancement automatisé d’un navigateur Chrome (via Selenium + webdriver-manager).

Exécution de scénarios d’automatisation (remplissage de formulaires, recherche Google, ping de pages, screenshots).

Exposition d’une API avec FastAPI pour piloter le bot.

Capture et sauvegarde de captures d’écran dans /screenshots.

Suite de tests complète (pytest) pour valider le bon fonctionnement.

## 📂 Structure du projet
bot-automatisation/
├─ bot/
│  ├─ __init__.py          # Initialisation du module
│  ├─ models.py            # Schémas Pydantic pour l'API
│  ├─ selenium_helper.py   # Fonctions utilitaires Selenium
│
├─ screenshots/            # Captures générées par le bot
│  └─ screenshot_xxx.png
│
├─ tests/                  # Tests unitaires & fonctionnels
│  ├─ smoke_test.py
│  ├─ test_bot_status.py
│  ├─ test_fill_form.py
│  ├─ test_google_search.py
│  ├─ test_ping.py
│  ├─ test_screenshot.py
│
├─ .env.example            # Variables d'environnement (exemple)
├─ .gitignore
├─ README.md
├─ conftest.py             # Configuration pytest
├─ main.py                 # Entrée principale FastAPI
├─ pyproject.toml          # Config formatage/linters (Black, Ruff)
├─ requirements.txt        # Dépendances
└─ screenshot.png          # Exemple de capture

## ⚙️ Installation & utilisation

1️⃣ Cloner le projet
git clone https://github.com/atmitim/portfolio_python.git
cd portfolio_python

2️⃣ Créer un environnement virtuel
python -m venv .venv
source .venv/Scripts/activate   # Windows
# ou
source .venv/bin/activate       # Linux / macOS

3️⃣ Installer les dépendances
pip install -r requirements.txt

4️⃣ Configurer les variables d’environnement

Copier .env.example → .env et ajuster les valeurs si nécessaire.

5️⃣ Lancer le bot (API FastAPI)
uvicorn main:app --reload


L’API sera dispo sur : http://127.0.0.1:8000

🧪 Lancer les tests
pytest -q


Tous les tests (tests/) doivent passer ✅.

## 🛠️ Technologies utilisées

Python 3.13

FastAPI (API)

Selenium + webdriver-manager (automatisation web)

Pytest (tests)

Pydantic (validation)

dotenv (gestion config)

Black / Ruff (formatage & linting)

## 📸 Exemple de screenshot

Voici un exemple de capture générée automatiquement par le bot avec **Selenium** :  

![Exemple Screenshot](screenshots/screenshot.png)

👤 Contact

Yahya Atmitim
📧 atmitimyahya@outlook.fr

🌍 GitHub – atmitim