# Portfolio Python 🐍

Bienvenue dans mon portfolio Python !  
Ce dépôt regroupe plusieurs projets réalisés dans le cadre de mes apprentissages et expérimentations en développement.  
Chaque projet illustre des compétences spécifiques en Python : automatisation, scraping, API, tests, et organisation de code.

---

## 📂 Projets inclus

### 1. Bot Automatisation 🤖
- **Description** : Un bot développé en Python pour automatiser certaines tâches répétitives (navigation web, formulaires, screenshots, etc.).
- **Technologies utilisées** : `selenium`, `pytest`, `python-dotenv`
- **Fonctionnalités** :
  - Interaction avec des pages web
  - Génération de captures d’écran
  - Tests automatisés
- 📁 [Dossier du projet](./bot_automatisation)

---

### 2. API Rapport 📊
- **Description** : Une API Python permettant de générer et gérer des rapports.
- **Technologies utilisées** : `FastAPI`, `Pydantic`
- **Fonctionnalités** :
  - Endpoints REST pour la création et la récupération de rapports
  - Gestion de la configuration via fichiers `.env`
- 📁 [Dossier du projet](./api-rapport)

---

### 3. Scraper Emplois 🔍
- **Description** : Un scraper d’offres d’emploi développé en Python.
- **Technologies utilisées** : `BeautifulSoup`, `requests`
- **Fonctionnalités** :
  - Extraction d’annonces depuis Indeed
  - Sauvegarde des pages HTML
  - Analyse des données collectées
- 📁 [Dossier du projet](./scraper-emplois)

---

## 🚀 Installation & Utilisation

Clonez le dépôt :

```bash```
git clone https://github.com/atmitim/portfolio-python.git
cd portfolio-python

Chaque projet contient son propre fichier requirements.txt ou pyproject.toml.

## Installez les dépendances dans un environnement virtuel :

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

✅ Tests

Certains projets contiennent des tests unitaires. Pour les exécuter : 

pytest

📌 Auteur

👤 ATMITIM Yahya
🔗 profil GitHub : atmitim