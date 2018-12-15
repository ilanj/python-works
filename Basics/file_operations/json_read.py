import json

with open('C:\\Users\\auxouser\\Desktop\\test\\ilanchezhian_json.txt') as json_file:
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