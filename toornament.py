# importing the requests library
import requests
import configparser

from team import Team

apiUrl = "https://api.toornament.com/viewer/v2"


def getTeamByTournamentIdAndName(tid, name):
    apiKey = readConfig()
    headers = {'X-Api-Key': apiKey, 'Range': 'participants=0-49'}
    r = requests.get(apiUrl + "/tournaments/"+tid+"/participants", headers=headers, params={"name": name})
    data = r.json()

    lineup = data[0]['lineup']
    players = []

    for l in lineup:
        players.append(l['custom_fields']['summoner_name'])

    team = Team(teamId=data[0]['id'], name=data[0]['name'], players=players)
    return team


def getMatchesByIdAndTeamId(tid, teamId):
    apiKey = readConfig()
    headers = {'X-Api-Key': apiKey, 'Range': 'matches=0-20'}
    r = requests.get(apiUrl + "/tournaments/" + tid + "/matches", headers=headers, params={"participant_ids": teamId})
    data = r.json()
    return data


def readConfig():
    config = configparser.ConfigParser()
    config.read('API_keys.ini')
    return config['toornament']['apiKey']


