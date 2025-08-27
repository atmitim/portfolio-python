# Scraper Emplois - Orthoptistes en France

![Python](https://img.shields.io/badge/python-3.13-blue)
![Selenium](https://img.shields.io/badge/selenium-4.14-orange)
![Status](https://img.shields.io/badge/status-fonctionnel-brightgreen)

Ce projet est un **scraper d’offres d’emploi** pour le métier d’**orthoptiste** en France, utilisant **Selenium** pour gérer les pages dynamiques du site [OptionCarriere](https://www.optioncarriere.com).

---

## Fonctionnalités

- Scraping complet des offres en France
- Parcours automatique de plusieurs pages
- Extraction des informations :
  - Titre du poste
  - Entreprise
  - Localisation
  - Lien vers l’annonce
- Sauvegarde automatique dans un fichier CSV (`jobs.csv`)
- Gestion des pages vides pour éviter les boucles infinies
- Configuration facile via le fichier `.env`

---

## Structure du projet

scraper-emplois/
├─ .venv/ # Environnement virtuel
├─ main.py # Script principal du scraper
├─ smoke_test.py # Test rapide du fonctionnement des packages
├─ requirements.txt # Liste des packages Python
├─ README.md # Documentation du projet
├─ .env.example # Exemple de fichier de variables d’environnement
├─ .env # Fichier réel des variables (non partagé sur GitHub)
├─ pyproject.toml # Configuration Black/Ruff
└─ .gitignore # Fichiers/dossiers à ignorer par Git

## Installation

1. **Cloner le projet :**

git clone https://github.com/ton-utilisateur/scraper-emplois.git
cd scraper-emplois

2. **Créer un environnement virtuel et installer les dépendences:** 

python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

3. **Configuer le fichier .env :**
API_KEY=
TARGET_URL=https://www.optioncarriere.com/emploi?s=orthoptiste&l=France

Lancer le scraper :
python main.py

Le script parcourt les pages des offres et sauvegarde les annonces dans jobs.csv.
Le scraping s’arrête automatiquement si une page ne contient aucune offre.
Pour visualiser le navigateur pendant le scraping, supprimer l’option --headless dans le script.

5. **Personnalisation**

Modifier la variable TARGET_URL dans le .env pour scraper un autre métier ou une autre localisation.
La structure du CSV reste la même.

6. **Exemple de résultat(job.csv)**
title,company,location,link
Orthoptiste - CDI Temps partiel (25%) F/H,AESIO Sante,Saint-Étienne,https://www.optioncarriere.com/jobad/fr565880c7cb123a974ba19c40a0d592b5
Orthoptiste dans le quartier d'affaires de la Défense H/F,Carrefour,Nanterre,https://www.optioncarriere.com/jobad/frad46c4f50247d98f88ec6ab66b92aeec

7. **Bonnes pratiques**

Ajouter un time.sleep() entre les pages pour réduire le risque de blocage.

Les erreurs affichées par Chrome (ex. DevTools listening, voice_transcription) sont normales et ne bloquent pas le scraping.

Vérifier régulièrement que le sélecteur CSS pour les annonces (article.job.clicky) correspond bien à la structure du site.

## Contact

Pour toute question ou collaboration :
**Email :** [atmitimyahya@outlook.fr](mailto:atmitimyahya@outlook.fr)  
**GitHub :** [atmitim](https://github.com/atmitim)

