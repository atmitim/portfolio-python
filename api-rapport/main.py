from fastapi import FastAPI
from app.api.routes import router
from app.core import config

app = FastAPI(
    title="API Report",
    description="API professionnelle pour générer et exposer des rapports CSV, Excel et PDF",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello API Rapport!", "base_url": config.BASE_URL}

