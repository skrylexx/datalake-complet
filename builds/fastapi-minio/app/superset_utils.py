import requests

SUPERSET_URL = "http://superset:8088"

def get_superset_data():
    response = requests.get(f"{SUPERSET_URL}/api/v1/chart")
    return response.json()
