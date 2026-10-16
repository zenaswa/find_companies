import requests

url = "https://recherche-entreprises.api.gouv.fr/near_point"
params = {
    "lat": "49.4432",
    "long": "1.0999",
    "radius": "50",
    "per_page": 10,
}

r = requests.get(url, params=params)

if r.status_code != 200:
    print(f"Error {r.status_code}: {r.text}")
else:
    data = r.json()
    print(f"Total: {data.get('total_results')}")
    for c in data["results"]:
        siege = c.get("siege", {})
        print(c["nom_complet"], "|", siege.get("adresse"))
