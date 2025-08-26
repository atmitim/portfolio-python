import requests
from fastapi import FastAPI

print("✅ API Rapport : Packages installés")

# Test rapide : vérifier FastAPI fonctionne
app = FastAPI()
print("FastAPI instance créée :", isinstance(app, FastAPI))
