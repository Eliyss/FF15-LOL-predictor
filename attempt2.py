import requests

payload = {"api_key":"30ebfcd2e818fd77f872aa2fa8c5d068"}
r = requests.get("http://api.champion.gg/stats", params = payload)
page = r.json()
champ = "Ezreal"
champData = requests.get("http://api.champion.gg/stats/champs/" + champ, params = payload)
page = champData.json()
print(page)