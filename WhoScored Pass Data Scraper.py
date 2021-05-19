import json
import pandas as pd

with open('C:/Football Analytics/CSV Data/ASVMUN.json') as f:
    data = json.load(f)

pi = []
player = []
x = []
y = []
endx = []
endy = []
team = []
outcome = []
minute = []
goal_x = []
goal_y = []
cx = []
cy = []
cendx = []
cendy = []
cplayer = []

for a, b in data.items():
    if a == 'playerIdNameDictionary':
        for i, n in b.items():
            pi.append([i, n])

for k in data['events']:
    if k['type']['displayName'] == 'Pass':
        for par, v in k.items():
            if par == 'x':
                x.append(v)
            if par == 'y':
                y.append(v)
            if par == 'playerId':
                for c, d in pi:
                    if str(v) == c:
                        player.append(d)
            if par == 'endX':
                endx.append(v)
            if par == 'endY':
                endy.append(v)
            if par == 'teamId':
                team.append(v)
            if par == 'outcomeType':
                outcome.append(k['outcomeType']['displayName'])
            if par == 'minute':
                minute.append(v)

for w in data['events']:
    if w['type']['displayName'] == 'Goal':
        for c, d in w.items():
            if c == 'x':
                goal_x.append(d)
            if c == 'y':
                goal_y.append(d)

col_names = ['player','x','y','endx','endy','team','outcome', 'minute', 'goalx', 'goaly']
df = pd.DataFrame([player,x,y,endx,endy,team,outcome,minute,goal_x,goal_y], index = col_names)
df = df.T
print(df)

df.to_csv('C:\Football Analytics\CSV Data\ASVMUN.csv')
