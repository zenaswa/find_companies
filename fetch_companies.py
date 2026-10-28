import requests

url = "https://recherche-entreprises.api.gouv.fr/near_point"
params = {
    "lat": "49.4432",
    "long": "1.0999",
    "radius": "30",
    "activite_principale": "62.01Z,62.02A,62.02B,62.03Z,62.09Z",
    "per_page": 10,
}

r = requests.get(url, params=params)

if r.status_code != 200:
    print(f"Error {r.status_code}: {r.text}")
else:
    data = r.json()
    print(f"Total: {data.get('total_results')}")
    for c in data["results"]:
        matching = c.get("matching_etablissements", [])
        for etab in matching:
            print(c["nom_complet"], "|", etab.get("adresse"))
