#

print("\nImportacao e uso de modulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"solicitracao http para {url} retornou o status {response.status_code}")