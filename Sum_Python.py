import requests

def obtener_goles_cristiano():
    url = "https://api.football-data.org/v2/players/CR7"
    headers = {"X-Auth-Token": "TU_API_KEY"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_goles = data["goals"]["total"]
        return total_goles
    else:
        return None

goles_cristiano = obtener_goles_cristiano()
if goles_cristiano is not None:
    print("Cristiano Ronaldo ha marcado", goles_cristiano, "goles.")
else:
    print("No se pudo obtener la información de los goles de Cristiano Ronaldo.")
