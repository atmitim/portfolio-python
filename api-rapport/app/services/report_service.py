import os
import json
import pandas as pd
from datetime import datetime
from fpdf import FPDF

REPORTS_DIR = "reports"
HISTORY_FILE = os.path.join(REPORTS_DIR, "history.json")
os.makedirs(REPORTS_DIR, exist_ok=True)

def save_history(entry):
    """Sauvegarde une entrée dans history.json"""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            history = []
    else:
        history = []

    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def generate_report(data):
    """Génère CSV et Excel et met à jour l'historique"""
    title = data["title"]
    start_date = str(data["start_date"])
    end_date = str(data["end_date"])
    generated_at = datetime.now().isoformat()

    df = pd.DataFrame([{"title": title, "start_date": start_date, "end_date": end_date}])

    csv_file = os.path.join(REPORTS_DIR, f"{title.replace(' ', '_')}_{generated_at.replace(':','').replace('.','')}.csv")
    excel_file = csv_file.replace(".csv", ".xlsx")

    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False)

    entry = {
        "title": title,
        "start_date": start_date,
        "end_date": end_date,
        "generated_at": generated_at,
        "csv_file": csv_file,
        "excel_file": excel_file
    }

    # Générer PDF
    pdf_file = csv_file.replace(".csv", ".pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Rapport: {title}", ln=True)
    pdf.cell(0, 10, f"Dates: {start_date} - {end_date}", ln=True)
    pdf.cell(0, 10, f"Généré le: {generated_at}", ln=True)
    pdf.output(pdf_file)
    entry["pdf_file"] = pdf_file

    save_history(entry)
    return entry

def list_reports(title=None, start_date=None, end_date=None):
    """Retourne les rapports filtrés"""
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    filtered = []
    for r in history:
        if title and title.lower() not in r["title"].lower():
            continue
        if start_date and r["start_date"] < start_date:
            continue
        if end_date and r["end_date"] > end_date:
            continue
        filtered.append(r)
    return filtered
