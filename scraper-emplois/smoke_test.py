import requests
from bs4 import BeautifulSoup
import pandas as pd

print("✅ Python et packages installés !")

# Test 1 : Requête HTTP
resp = requests.get("https://httpbin.org/html")
print("Requête OK :", resp.status_code)

# Test 2 : Parsing HTML
soup = BeautifulSoup(resp.text, "lxml")
print("Titre de la page :", soup.find("h1").text)

# Test 3 : Pandas DataFrame
df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
print("DataFrame :")
print(df)
