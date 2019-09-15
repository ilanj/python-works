import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/ai', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def user():
    if request.method == 'GET':
        data={
	"name": "saranya",
	"company": "concord",
	"leaves": [7, 15, 22, 27],
	"location": {
		"native": "pondicherry",
		"working": {
			"devteam": "kerala",
			"testteam": "chennai",
			"headofice": "seattle"
		}
	}
}
        empdetails=json.dumps(data)
        return empdetails


if __name__ == '__main__':
    app.run(debug=True)