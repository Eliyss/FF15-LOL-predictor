import requests

payload = {"api_key":"RGAPI-323252c0-2ba4-4ede-8c29-005f1133d4c0"}
r = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/Eliyss", params = payload)
page = r.json()
accID = page["accountId"]
print(accID)
soloQPayload = {
    "api_key":"RGAPI-323252c0-2ba4-4ede-8c29-005f1133d4c0",
    "endIndex":20,
    "queue":420,
    "season":11
}
matchlist = requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accID), params = soloQPayload)
page = matchlist.json()
gameIDs = []
for i in range(len(page["matches"])):
    asd.append(page["matches"][i]["gameId"])

print(asd)


