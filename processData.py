import pandas as pd
import json

"""
csvtojson = pd.read_csv('data/besta_report_data_2024.csv')
csvtojson.to_json('data/besta_report_data_2024.json',orient='records')"""

with open( 'data/besta_report_data_2024.json', 'r') as data:
    data = json.load(data)

teams = []
teamData = {}
for d in data:
    if d['team'] not in teams:
        teams.append(d['team'])
        teamData[d['team']] = {
            'team':d['team'],
            'xG':0,
            'xGA':0,
            'shots':0,
            'shotsAgainst':0,
            'shotsOutsideBox':0,
            'shotsOutsideBoxFaced':0
        }
    if d['opponent'] not in teams:
        teams.append(d['opponent'])
        teamData[d['opponent']] = {
            'team':d['opponent'],
            'xG':0,
            'xGA':0,
            'shots':0,
            'shotsAgainst':0,
            'shotsOutsideBox':0,
            'shotsOutsideBoxFaced':0
        }
    #print(d)
    if d['xg'] != None:
        teamData[d['team']]['xG'] += d['xg']
        teamData[d['opponent']]['xGA'] += d['xg']
        teamData[d['team']]['shots'] += d['shots']
        teamData[d['opponent']]['shotsAgainst'] += d['shots']
        teamData[d['team']]['shotsOutsideBox'] += d['shots_outside_box']
        teamData[d['opponent']]['shotsOutsideBoxFaced'] += d['shots_outside_box']

finalData = []
for team in teams:
    
    teamData[team]['xG'] = round(teamData[team]['xG'],2)
    teamData[team]['xGA'] = round(teamData[team]['xGA'],2)
    teamData[team]['xGDiff'] = round(teamData[team]['xG'] - teamData[team]['xGA'],2)
    teamData[team]['SOBRatio'] = round(teamData[team]['shotsOutsideBox'] / teamData[team]['shots'],2)
    teamData[team]['SOBARatio'] = round(teamData[team]['shotsOutsideBoxFaced'] / teamData[team]['shotsAgainst'],2)
    finalData.append(teamData[team])
finalData = sorted(finalData, key=lambda d:d['xGDiff'], reverse=True)
    
    


"""
teamData = {
    "ÍA":{
        home_games:
        away_games:
        home_xG:
        away_xG:
    }

}
"""
for team in finalData:
    print(team)