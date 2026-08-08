import requests

HUD_API = "https://egis.hud.gov/arcgis/rest/services/cpdmaps/HudSfReo/MapServer/0/query"

params = {
    "where": "1=1",
    "outFields": "*",
    "returnGeometry": "false",
    "f": "json"
}

response = requests.get(HUD_API, params=params)
data = response.json()

properties = data.get("features", [])

print(f"🏠 Found {len(properties)} HUD properties")

for property in properties[:10]:
    print(property["attributes"])