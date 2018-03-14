import requests

def getWinRate(champ, role):
    payload = {"api_key":"30ebfcd2e818fd77f872aa2fa8c5d068"}
    r = requests.get("http://api.champion.gg/stats/champs/" + champ, params = payload)
    page = r.json()
    print(page)
    length = len(page)
    winRate = 0
    for i in range(length):
        isRole = page[i].get("Role", default = "None")
        if (role == isRole):
            return page[i]["general"]["winPercent"]
        
        winRate = winRate + page[i]["general"]["winPercent"]
    
    return winRate / length

def getMatchupWinRate(champ, opponent, role):
    payload = {"api_key":"30ebfcd2e818fd77f872aa2fa8c5d068"}
    r = requests.get("http://api.champion.gg/champion/" + champ + "/matchup/" + opponent, params = payload)
    page = r.json()
    if ("error" in page):
        return 50.00
    
    print(page)
    length = len(page)
    for i in range(length):
        isRole = page[i].get("role", default = "None")
        if (role == isRole):
            return page[i]["general"]["winRate"]

    return 50.00



print(getMatchupWinRate("Annie", "Aatrox", "Middle"))

