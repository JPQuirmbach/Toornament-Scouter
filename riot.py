import requests
import configparser

apiUrl = "https://euw1.api.riotgames.com"


def getAccountIdByName(name):
    apiKey = readConfig()
    headers = {'X-Riot-Token': apiKey}
    r = requests.get(apiUrl + "/lol/summoner/v3/summoners/by-name/"+name, headers=headers)
    data = r.json()
    return data['accountId']


def getMatchList(accountId):
    apiKey = readConfig()
    headers = {'X-Riot-Token': apiKey}
    params = {'queue': 420, 'season': 11}
    r = requests.get(apiUrl + "/lol/match/v3/matchlists/by-account/" + str(accountId), headers=headers, params=params)
    data = r.json()
    return data


def readConfig():
    config = configparser.ConfigParser()
    config.read('API_keys.ini')
    return config['riot']['apiKey']


