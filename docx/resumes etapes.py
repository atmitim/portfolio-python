from fpdf import FPDF

# Création du PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)

# Titre
pdf.cell(0, 10, "Plan d'Installation et de Mise en Place Python - Portfolio", ln=True, align="C")

pdf.ln(10)

pdf.set_font("Arial", "", 12)

# Contenu du PDF
content = """
# 1) Installation de Python

### Windows
1. Télécharger Python 3.12+ depuis python.org.
2. Cocher "Add python.exe to PATH" pendant l'installation.
3. Vérifier:
   python --version
   pip --version

### macOS
brew install python
python3 --version

### Linux (Debian/Ubuntu)
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version

# 2) Installation de VS Code
1. Télécharger VS Code depuis code.visualstudio.com.
2. Installer les extensions:
   - Python (ms-python.python)
   - Pylance
   - Ruff
   - Jupyter
   - GitLens

# 3) Installation de Git et configuration
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@exemple.com"
git config --global init.defaultBranch main

# 4) Création du repo "portfolio-python"
mkdir portfolio-python && cd portfolio-python
git init
echo "# Portfolio Python" > README.md
echo ".venv/" > .gitignore

# Arborescence
portfolio-python/
  scraper-emplois/
  bot-automatisation/
  api-rapport/

# 5) Environnements virtuels pour chaque projet
cd scraper-emplois
python -m venv .venv
source .venv/Scripts/activate  # Windows
python -m pip install --upgrade pip
pip install requests beautifulsoup4 lxml pandas pytest python-dotenv black ruff
pip freeze > requirements.txt
deactivate

# Même chose pour bot-automatisation et api-rapport avec leurs dépendances spécifiques

# 6) Ouvrir dans VS Code + sélectionner l'interpréteur
- Ouvrir le dossier dans VS Code (Fichier → Ouvrir dossier ou code .)
- Sélectionner l'interpréteur Python correspondant au venv:
  Ctrl+Shift+P → Python: Select Interpreter → choisir .venv/Scripts/python.exe
- Vérifier dans le terminal intégré: which python

# 7) Smoke Tests (tester que Python + packages fonctionnent)
- Scraper
- Bot
- API

# 8) Templates utiles pour chaque projet
- README.md
- .env.example
- .gitignore

# 9) Premier commit
git add .
git commit -m "chore: bootstrap monorepo + squelettes projets + deps"

# 10) Spécifications rapides des 3 projets
1. Scraper d'annonces
2. Bot d'automatisation
3. Script API → Rapport

# Notes importantes
- Sous Windows, les chemins des venv sont `.venv/Scripts/` et pas `bin/`
- Toujours désactiver un venv avant d'en activer un autre: deactivate
- VS Code doit pointer sur l'interpréteur correct pour chaque projet

# Étapes suivantes
- Commencer le développement du Scraper
- Tester Selenium pour le Bot
- Tester API pour le script de rapport
- Créer le portfolio GitHub
- Préparer les offres freelance
"""

# Ajouter le contenu au PDF
for line in content.split("\n"):
    pdf.multi_cell(0, 6, line)

# Sauvegarder le PDF
file_path = "/mnt/data/Plan_Portfolio_Python.pdf"
pdf.output(file_path)
file_path
