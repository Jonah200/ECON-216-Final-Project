import pandas as pd
import json

with open("fangraphs.json", "r") as f:
    data = json.load(f)

frame = pd.DataFrame(data['data'])
frame['Name'] = frame['PlayerName']
frame['Team'] = frame['TeamName']
frame.to_csv("fangraphs.csv")
print(frame)