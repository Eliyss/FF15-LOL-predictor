import requests
from champions import *

apiKey = "RGAPI-2e0f5266-f3e7-4295-8aa8-26405e20d44b"

def getAccountId(name):
    payload = {
        "api_key":apiKey
    }

    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name, params = payload)
    page = r.json()
    return page["accountId"]

def getSummonerId(name):
    payload = {
        "api_key":apiKey
    }

    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name, params = payload)
    page = r.json()
    return page["summonerId"]

def getMatchList(accountId):
    payload = {
        "api_key":apiKey,
        "endIndex":25,
        "queue":420,
        "season":11,
    }

    matchlist = requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accountId), params = payload)
    page = matchlist.json()
    gameIds = []

    for i in range(len(page["matches"])):
        gameIds.append(page["matches"][i]["gameId"])

    return gameIds

### now redundant ###
# def getMatchList(accountId, champId):
#     payload = {
#         "api_key":apiKey,
#         "endIndex":25,
#         "queue":420,
#         "season":11,
#         "champion":champId
#     }
# 
#     matchlist = requests.get("https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(accountId), params = payload)
#     page = matchlist.json()
#     gameIds = []
# 
#     for i in range(len(page["matches"])):
#         gameIds.append(page["matches"][i]["gameId"])
# 
#     return gameIds
# 
# def getMatchOutcome(matchId, accountId):
#     payload = {
#         "api_key":apiKey,
#     }
# 
#     match = requests.get("https://na1.api.riotgames.com/lol/match/v3/matches/" + str(matchId), params = payload)
#     page = match.json()
# 
#     blueSide = False
#     for i in range(10):
#         if page["participantIdentities"][i]["player"]["accountId"] == accountId:
#             if page["participantIdentities"][i]["participantId"] < 6:
#                 blueSide = True
#                 break
#     
#     blueSideWin = False
#     if page["teams"][0]["win"] == "Win":
#         blueSideWin = True
#     
#     if blueSide == blueSideWin:
#         return 1
#     return 0
# 
# def getWinRate(accountName, champ):
#     accountId = getAccountId(accountName)
#     champId = convertChamptoId(champ)
#     matchList = getMatchList(accountId, champId)
#     matches = len(matchList)
# 
#     if matches < 10:
#         return 0.50
# 
#     wins = 0
#     for i in range(matches):
#         wins += getMatchOutcome(matchList[i], accountId)
#     return round(wins/matches, 2)