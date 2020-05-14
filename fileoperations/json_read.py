import json

with open('G:\workspace\pythontutorial\json_ex.txt') as json_file:
    data = dict(json.load(json_file))
    print(data)
for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
print(data)
for x,y in data.items():
    print(x,y)
