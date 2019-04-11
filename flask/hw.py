import json

from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    status=True
    data = {"faxCoversheet": status, "name": "ila",
        "place": "chennai",
        "id": 36,
        12: 25,
        14: "sddd"
            }
    data_json = json.dumps(data)

    n=6
    if n%2 is 0:
        return data_json
    else:
        return data_json

if __name__=="__main__":
    app.run(debug=True)