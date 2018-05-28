import requests
import pandas as pd
import requests_cache
import numpy as np
requests_cache.install_cache('amazon3', backend='sqlite', expire_after=7200)

top, jg, mid, adc, supp = [], [], [], [], []

win = []

for j in range(1,11):
    r = requests.get('https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches'+str(j)+'.json')
    print(str(r.from_cache) + ' ' + str(j))
    page = r.json()

    for i in range(100):

        team = [0, 0, 0, 0, 0]
        
        valid = True
        for k in range(5):
            if (page['matches'][i]['participants'][k]['timeline']['lane'] == 'TOP'):
                team[0] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['lane'] == 'JUNGLE'):
                team[1] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['lane'] == 'MIDDLE'):
                team[2] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['role'] == 'DUO_CARRY'):
                team[3] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['role'] == 'DUO_SUPPORT'):
                team[4] = page['matches'][i]['participants'][k]['championId']
        
        for k in range(5):
            if (team[k] == 0):
                valid = False
        
        if (valid):
            top.append(team[0])
            jg.append(team[1])
            mid.append(team[2])
            adc.append(team[3])
            supp.append(team[4])
            win.append(page['matches'][i]['teams'][0]['win'] == 'Win')
        
        team = [0, 0, 0, 0, 0]
        
        valid = True
        for k in range(5, 10):
            if (page['matches'][i]['participants'][k]['timeline']['lane'] == 'TOP'):
                team[0] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['lane'] == 'JUNGLE'):
                team[1] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['lane'] == 'MIDDLE'):
                team[2] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['role'] == 'DUO_CARRY'):
                team[3] = page['matches'][i]['participants'][k]['championId']
            elif (page['matches'][i]['participants'][k]['timeline']['role'] == 'DUO_SUPPORT'):
                team[4] = page['matches'][i]['participants'][k]['championId']
        
        for k in range(5):
            if (team[k] == 0):
                valid = False
        
        if (valid):
            top.append(team[0])
            jg.append(team[1])
            mid.append(team[2])
            adc.append(team[3])
            supp.append(team[4])
            win.append(page['matches'][i]['teams'][1]['win'] == 'Win')

d = {'top' : pd.Series(top),
     'jg' : pd.Series(jg),
     'mid' : pd.Series(mid),
     'adc' : pd.Series(adc),
     'supp' : pd.Series(supp),
     'win' : pd.Series(win)}
    
df = pd.DataFrame(d)

print(df)

df.to_csv('roles.csv')
