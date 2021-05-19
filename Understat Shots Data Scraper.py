import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json
import pandas as pd

url = input("Enter link: ")                         #Sample link = https://understat.com/match/15762
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('script')

strdata = str(tags[1])
ind_start = strdata.index("('")
ind_end = strdata.index("')")
strdata = strdata[ind_start+2:ind_end]
json_data = strdata.encode('utf8').decode('unicode_escape')

data = json.loads(json_data)
print(json.dumps(data, indent = 2))

data_home = data['h']
data_away = data['a']
xg = []
player = []
result = []
x = []
y = []
team = []

for shots in data_home:
    for p,v in shots.items():
        if p == 'result':
            result.append(v)
        if p == 'xG':
            xg.append(v)
        if p == 'h_team':
            team.append(v)
        if p == 'X':
            x.append(v)
        if p == 'Y':
            y.append(v)
        if p == 'player':
            player.append(v)

for shots in data_away:
    for p,v in shots.items():
        if p == 'result':
            result.append(v)
        if p == 'xG':
            xg.append(v)
        if p == 'a_team':
            team.append(v)
        if p == 'X':
            x.append(v)
        if p == 'Y':
            y.append(v)
        if p == 'player':
            player.append(v)

col_names = ['player', 'X', 'Y', 'xG', 'result', 'team']
df = pd.DataFrame([player,x,y,xg,result,team], index = col_names)
df = df.T
print(df)
df.to_csv("C:\Football Analytics\CSV Data\Ronaldo Shots Data.csv")