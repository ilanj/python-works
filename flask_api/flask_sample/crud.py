import json
from flask import Flask, request
from werkzeug.utils import secure_filename

from flask_api.flask_sample.Mongohelper import Mongohelper

connect_db=Mongohelper()

app = Flask(__name__)

@app.route('/ai/<user_id>', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        print(user_id)
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

    if request.method == 'POST':
        data = request.get_json()
        return json.dumps(data)

    if request.method == 'PUT':
        data = request.get_json()
        return json.dumps(data)

    if request.method == 'DELETE':
        data = request.get_json()
        return json.dumps(data)

@app.route('/test/<_id>', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def connectdb(_id):
    if request.method == 'GET':
        # _id = request.get_json()
        data=connect_db.readdb(_id)
        return data

    if request.method == 'POST':
        data=request.get_json()
        _id=connect_db.insert_doc(data)
        data={"_id":_id}
        return json.dumps(data)

@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == 'POST':
        f = request.files['file']
        f.save('D:/backups/' + secure_filename(f.filename))
        return 'file uploaded successfully'



if __name__ == '__main__':
    app.run(debug=True)