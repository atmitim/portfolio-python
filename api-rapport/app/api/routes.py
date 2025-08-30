from fastapi import APIRouter, Query
from typing import Optional
from app.services.report_service import generate_report, list_reports

router = APIRouter()

@router.post("/generate-report")
def create_report(payload: dict):
    try:
        report = generate_report(payload)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@router.get("/reports")
def get_reports(
    title: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
):
    reports = list_reports(title, start_date, end_date)
    return {"reports": reports}

from fastapi.responses import FileResponse

@router.get("/download")
def download_report(file: str):
    """Télécharge un fichier CSV, Excel ou PDF"""
    if not os.path.exists(file):
        return {"status": "error", "detail": "Fichier introuvable"}
    return FileResponse(path=file, filename=os.path.basename(file), media_type="application/octet-stream")

