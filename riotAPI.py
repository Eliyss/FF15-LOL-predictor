import requests
from champList import *

def getAccountId(name, apiKey):
    payload = {
        "api_key":apiKey
    }

    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name, params = payload)
    page = r.json()
    return page["accountId"]

def getMatchList(accountId, champId, apiKey):
    payload = {
        "api_key":apiKey,
        "endIndex":25,
        "queue":420,
        "season":11,
        "champion":champId
    }

    matchlist = requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accountId), params = payload)
    page = matchlist.json()
    gameIds = []

    for i in range(len(page["matches"])):
        gameIds.append(page["matches"][i]["gameId"])

    return gameIds

def getMatchOutcome(matchId, accountId, apiKey):
    payload = {
        "api_key":apiKey,
    }

    match = requests.get("https://na1.api.riotgames.com/lol/match/v3/matches/" + str(matchId), params = payload)
    page = match.json()

    blueSide = False
    for i in range(10):
        if page["participantIdentities"][i]["player"]["accountId"] == accountId:
            if page["participantIdentities"][i]["participantId"] < 6:
                blueSide = True
                break
    
    blueSideWin = False
    if page["teams"][0]["win"] == "Win":
        blueSideWin = True
    
    if blueSide == blueSideWin:
        return 1
    return 0

def getWinRate(accountName, champ, apiKey):
    accountId = getAccountId(accountName, apiKey)
    champId = convertChamptoId(champ)
    matchList = getMatchList(accountId, champId, key)
    matches = len(matchList)

    if matches < 10:
        return 0.50

    wins = 0
    for i in range(matches):
        wins += getMatchOutcome(matchList[i], accountId, apiKey)
    return round(wins/matches, 2)


key = "RGAPI-2eb76d8e-38a7-4807-8c9a-edb24f3637e9"
print(getWinRate("eliyss", "Ekko", key))
