import requests
from champions import *

apiKey = 'RGAPI-2e0f5266-f3e7-4295-8aa8-26405e20d44b'
eliyssAccountId = 206524563
eliyssSummonerId = 44002226
sampleMatchId = 2742011660

def getAccountId(name):
    payload = {
        'api_key':apiKey
    }

    r = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name, params = payload)
    page = r.json()

    return page['accountId']

def getSummonerId(name):
    payload = {
        'api_key':apiKey
    }

    r = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + name, params = payload)
    page = r.json()

    return page['summonerId']

def getMatchList(accountId):
    payload = {
        'api_key':apiKey,
        'endIndex':5,
        'queue':420,
        'season':11,
    }

    matchlist = requests.get('https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(accountId), params = payload)
    page = matchlist.json()
    gameIds = []

    for i in range(len(page['matches'])):
        gameIds.append(page['matches'][i]['gameId'])

    return gameIds

def checkValidTeam(teamList):
    if teamList[-1]:
        team = [0, 0, 0, 0, 0]
        for i in range(5):
            if team[teamList[i]['position']]:
                return False
            else:
                team[teamList[i]['position']] = 1
        
        team = [0, 0, 0, 0, 0]
        for i in range(5, 10):
            if team[teamList[i]['position']]:
                return False
            else:
                team[teamList[i]['position']] = 1
        return True

    return False

def getMatchStats(matchId):
    payload = {
        'api_key':apiKey,
    }

    match = requests.get('https://na1.api.riotgames.com/lol/match/v3/matches/' + str(matchId), params = payload)
    page = match.json()

    matchInfo = []
    redWin = 0
    validComp = True
    
    for i in range(10):
        playerId = page['participantIdentities'][i]['player']['accountId']
        playerChampion = page['participants'][i]['championId']
        playerLane = page['participants'][i]['timeline']['lane']
        playerRole = page['participants'][i]['timeline']['role']

        if playerLane == 'TOP' and playerRole == 'SOLO':
            position = 0
        elif playerLane == 'JUNGLE' and playerRole == 'NONE':
            position = 1
        elif playerLane == 'MIDDLE' and playerRole == 'SOLO':
            position = 2
        elif playerLane == 'BOTTOM' and playerRole == 'DUO_CARRY':
            position = 3
        elif playerLane == 'BOTTOM' and playerRole == 'DUO_SUPPORT':
            position = 4 
        else:
            validComp = False

        if i < 5:
            team = 'blue'
        else:
            team = 'red'
        
        matchInfo.append(dict(accountId = playerId, championId = playerChampion, position = position, team = team))
    
    if not page['participants'][0]['stats']['win']:
        redWin = 1

    matchInfo.append(redWin)
    matchInfo.append(validComp)
    
    matchInfo[-1] = checkValidTeam(matchInfo)

    return matchInfo