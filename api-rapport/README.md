# 🚀 API Report

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/ton-utilisateur/ton-projet/actions)  
[![Tests](https://img.shields.io/badge/tests-smoke%20tested-blue)](smoke_test.py)  
[![Lint](https://img.shields.io/badge/linted-Ruff-yellow)](https://github.com/ton-utilisateur/ton-projet)  
[![Python Version](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

## 🔗 Liens rapides

- [Objectifs du projet](#-objectifs-du-projet)
- [Fonctionnalités principales](#-fonctionnalités-principales)
- [Technologies utilisées](#-technologies-utilisées)
- [Installation et setup](#-installation-et-setup)
- [Exemple d’utilisation](#-exemple-dutilisation)
- [Bonus pour les clients](#-bonus-pour-les-clients)
- [Tests rapides](#-tests-rapides)
- [Workflow / Diagramme visuel](#-workflow--diagramme-visuel)

API Report est une API moderne et sécurisée pour générer, consulter et télécharger des rapports personnalisés (CSV, Excel, PDF) à partir de vos données. Idéale pour les entreprises et les développeurs souhaitant automatiser la création de rapports et analyser rapidement des informations clés.

## 🔹 Objectifs du projet

Automatiser la génération de rapports.

Fournir les rapports sous un format exploitable (JSON, CSV, Excel, PDF).

Offrir une API simple, sécurisée et documentée pour faciliter l’intégration avec d’autres systèmes.

## 🔹 Fonctionnalités principales

✅ Endpoint de test : GET /
✅ Génération de rapports : POST /generate-report
✅ Export des rapports : CSV, Excel et PDF
⚡ Historique des rapports générés (history.json)
🔒 Sécurisation via clé API
📖 Documentation interactive (Swagger / Redoc)
🧪 Tests automatisés avec Pytest
📥 Téléchargement direct des fichiers via /download?file=...

## 🔹 Technologies utilisées

| Fonctionnalité          | Outils / Librairies       |
|-------------------------|---------------------------|
| Langage                 | Python 3.11+              |
| Framework API           | FastAPI                   |
| Manipulation des données| Pandas, FPDF              |
| Tests                   | Pytest                    |
| Formatage / Linting     | Black, Ruff               |
| Environnement           | Virtualenv / venv         |
| Configuration           | .env                      |

## 🔹 Installation et setup

### 1️⃣ Cloner le projet

git clone <URL_DU_PROJET>
cd api-report


### 2️⃣ Créer l’environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows

### 3️⃣ Installer les dépendances

pip install -r requirements.txt
pip install fpdf

### 4️⃣ Configurer les variables d’environnement
cp .env.example .env
Modifier .env avec votre API_KEY et BASE_URL

### 5️⃣ Démarrer l’API
uvicorn main:app --reload

### 6️⃣ Accéder à la documentation

Swagger : http://127.0.0.1:8000/docs

Redoc : http://127.0.0.1:8000/redoc

## 🔹 Exemple d’utilisation

### 1️⃣ Endpoint racine

GET /

Réponse :

{
  "message": "Hello API Rapport!",
  "base_url": "https://monapi.example.com"
}

### 2️⃣ Générer un rapport

POST /generate-report

{
    "title": "Ventes mensuelles",
    "start_date": "2025-08-01",
    "end_date": "2025-08-31"
}


Réponse :


{
  "status": "success",
  "report": {
    "title": "Ventes mensuelles",
    "start_date": "2025-08-01",
    "end_date": "2025-08-31",
    "generated_at": "2025-08-30T19:52:32.527338",
    "csv_file": "reports/Ventes_mensuelles_20250830_195232.csv",
    "excel_file": "reports/Ventes_mensuelles_20250830_195232.xlsx",
    "pdf_file": "reports/Ventes_mensuelles_20250830_195232.pdf"
  }
}

### 3️⃣ Lister tous les rapports

GET /reports

Filtrage possible avec : title, start_date, end_date

curl -X GET "http://127.0.0.1:8000/reports?title=Ventes&start_date=2025-08-01"

### 4️⃣ Télécharger un fichier

GET /download?file=reports/Ventes_mensuelles_20250830_195232.xlsx

Supporte CSV, Excel et PDF

## 🔹 Bonus pour les clients

Rapports exportables en CSV, Excel et PDF

Filtrage avancé des rapports

Historique complet des rapports générés

API prête à être intégrée dans des systèmes existants

Documentation interactive Swagger/Redoc pour tester facilement

## 🔹 Tests rapides
`python smoke_test.py`

Vérifie que FastAPI et l’environnement fonctionnent correctement

## 🔹 Workflow / Diagramme visuel

![Workflow API Report](docs/diagramme_api_report.png)

*Flux de génération d’un rapport → sauvegarde → téléchargement*