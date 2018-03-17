import urllib
from bs4 import BeautifulSoup

def getWinRate(champion, summonerId):
    url = "http://na.op.gg/summoner/champions/ajax/champions.rank/summonerId="+str(summonerId)+"&season=11&queueType=soloranked"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    champList = soup.find_all('td', class_ = "ChampionName Cell")
    winRates = soup.find_all('span', class_ = 'WinRatio normal')
    numChamps = len(champList)
    for i in range(numChamps):
        champName = champList[i]["data-value"]
        champName = champName.replace(" ","")
        champName = champName.replace("\'","")
        champName = champName.lower()

        if champName == champion:
            return int(winRates[i].string.strip('%'))
    
    return 50

print(getWinRate("ahri", 44002226))