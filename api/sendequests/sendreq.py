import requests
import pprint

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
# print(users)
pprint.pprint(users)