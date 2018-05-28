import requests
import requests_cache
import dailyInfo

requests_cache.install_cache('riot_static_data', backend='sqlite', expire_after=86400)

def idToName(id):
    payload = {
        'api_key':dailyInfo.apiKey,
        'dataById':'true'
    }

    r = requests.get('https://na1.api.riotgames.com//lol/static-data/v3/champions/', params = payload)
    page = r.json()

    if str(id) in page['data'] :
        return page['data'][str(id)]['name']

print(idToName(103))