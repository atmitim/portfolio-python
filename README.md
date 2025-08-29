# Bot Automatisation

![Python](https://img.shields.io/badge/python-3.13-blue)
![Smoke Tests](https://img.shields.io/badge/smoke-tests%20passed-brightgreen)

Bienvenue dans le projet **Bot Automatisation** !  
Ce projet permet d’automatiser des tâches répétitives sur le web grâce à **Selenium**, tout en utilisant des tests automatisés pour garantir le bon fonctionnement du bot.

---

## Description

Le bot peut :

- Remplir automatiquement des formulaires web.
- Effectuer des recherches sur Google et extraire des résultats.
- Prendre des captures d’écran des pages web.
- Vérifier le statut du bot et la connectivité internet.

Le projet inclut également des **smoke tests** pour valider rapidement l’installation et le fonctionnement du bot.

---

## Structure du projet

bot-automatisation/
├─ .venv/ # Environnement virtuel
├─ main.py # Script principal du bot
├─ bot/ # Modules du bot
├─ tests/ # Tests Pytest
│ ├─ test_fill_form.py
│ ├─ test_google_search.py
│ ├─ test_ping.py
│ ├─ test_screenshot.py
│ ├─ test_bot_status.py
│ └─ smoke_test.py
├─ conftest.py # Fixtures pour les tests
├─ requirements.txt # Dépendances Python
├─ screenshots/ # Captures d'écran générées par le bot
├─ screenshot.png # Exemple de capture d’écran
├─ README.md # Ce fichier
├─ pyproject.toml # Configuration pour l'éditeur et formatage
└─ .gitignore # Fichiers/dossiers à ignorer

## Technologies utilisées 

- Python 3.13  
- Selenium  
- requests  
- webdriver-manager  
- python-dotenv  
- pytest  
- black (formatage)  
- ruff (linting)  

## Installation et utilisation

1. Cloner le projet :

bash
git clone https://github.com/atmitim/portfolio-python.git
cd portfolio-python/bot-automatisation

2. Créer et activer l’environnement virtuel :

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

3. Installer les dépendances :

pip install -r requirements.txt

4. Copier le fichier d’exemple .env.example en .env et remplir les variables nécessaires (ex: TARGET_URL).

5. Lancer le smoke test pour vérifier que tout fonctionne correctement :

python tests/smoke_test.py


## Structure des tests

tests/smoke_test.py : test rapide pour vérifier que Selenium et requests fonctionnent.

tests/test_fill_form.py : test de remplissage de formulaire.

tests/test_google_search.py : test de recherche Google.

tests/test_ping.py : test de connectivité.

tests/test_screenshot.py : test de capture d’écran.

tests/test_bot_status.py : test du statut du bot.


## Contact

Pour toute question ou collaboration :

Email : atmitimyahya@outlook.fr
GitHub : atmitim




