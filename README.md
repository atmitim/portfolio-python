# Portfolio Python

Bienvenue dans mon **portfolio Python** !  
Ce repository contient trois projets distincts, chacun avec son propre environnement virtuel et ses dépendances, démontrant différentes compétences en **web scraping**, **automatisation** et **création d’API**.

---

## 1. Scraper Emplois

**Description :**  
Projet permettant de collecter des offres d’emploi depuis différents sites web, de les analyser et de les stocker pour un usage ultérieur.

**Structure :**

scraper-emplois/
├─ .venv/ # Environnement virtuel du projet
├─ main.py # Script principal
├─ smoke_test.py # Test rapide des dépendances
├─ requirements.txt # Liste des packages Python nécessaires
├─ README.md # README spécifique au projet
├─ .env.example # Exemple de fichier de variables d'environnement
├─ pyproject.toml # Configuration pour l'éditeur et formatage (Black, Ruff)
└─ .gitignore # Fichiers/dossiers à ignorer par Git

## 2. Bot Automatisation

**Description :**
Bot pour automatiser des tâches répétitives sur le web, en utilisant Selenium pour interagir avec les navigateurs et effectuer des actions automatiquement.

**Structure :**

bot-automatisation/
├─ .venv/
├─ main.py
├─ smoke_test.py
├─ requirements.txt
├─ README.md
├─ .env.example
├─ pyproject.toml
└─ .gitignore


Technologies utilisées :
Python, requests, Selenium, webdriver-manager, python-dotenv, pytest, black, ruff.

Exécuter le smoke test :

cd bot-automatisation
source .venv/Scripts/activate
python smoke_test.py


Vérifie que Selenium et requests sont installés et fonctionnent correctement.

Ouvre un navigateur Chrome via Selenium pour tester l’automatisation.

## 3. API Rapport

**Description :**
API pour générer et exposer des rapports de données, utilisant FastAPI. Elle peut être utilisée pour collecter, transformer et fournir des données à d’autres services.

**Structure :**

api-rapport/
├─ .venv/
├─ main.py
├─ smoke_test.py
├─ requirements.txt
├─ README.md
├─ .env.example
├─ pyproject.toml
└─ .gitignore


Technologies utilisées :
Python, FastAPI, requests, python-dotenv, pytest, black, ruff.

Exécuter le smoke test :

cd api-rapport
source .venv/Scripts/activate
python smoke_test.py


Vérifie que FastAPI et requests sont installés et que l’API peut être initialisée correctement.

## Instructions Générales

**Cloner le repository :**

git clone https://github.com/ton-username/portfolio-python.git
cd portfolio-python


Pour chaque projet :

cd <nom-du-projet>
python -m venv .venv               # Créer le venv si nécessaire
source .venv/Scripts/activate      # Activer le venv
pip install -r requirements.txt    # Installer les dépendances
python smoke_test.py               # Vérifier que tout fonctionne


Variables d’environnement :

Copier .env.example en .env et remplir les variables nécessaires à chaque projet (ex: TARGET_URL pour le bot).

## Structure générale du repository
portfolio-python/
├─ scraper-emplois/
├─ bot-automatisation/
├─ api-rapport/
└─ README.md


Chaque projet a son propre venv, requirements.txt et smoke_test.py pour tester rapidement le bon fonctionnement.


## Licence

Ce projet est sous licence MIT.
Voir le fichier LICENSE pour plus de détails.

## Contact

Pour toute question ou collaboration :
Email : atmitimyahya@outlook.fr

GitHub : atmitim