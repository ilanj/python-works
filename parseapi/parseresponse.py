import json

import requests

url = "http://localhost:2018/test/hello"

# payload = "5c544cf15b021885309160c9"
headers = {
    'Cache-Control': "no-cache",
    # 'Postman-Token': "64d4dff7-a5ba-4b3e-4f6b-9179ffb2c833"
    }

response = requests.request("GET", url, headers=headers)

# print(response.json())