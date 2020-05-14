import json

from bson import json_util, ObjectId
from pymongo import MongoClient

class Mongohelper:

    client = MongoClient("localhost", 27017)
    mydatabase = client["ila_practice"]  # If there is no previously created database with this name, MongoDB will implicitly create one for the user.
    mycollection = mydatabase['company_names']

    def insert_doc(self,data):
        # rec = {
        #     'title': 'MongoDB and Python 24 april',
        #     'description': 'MongoDB is no SQL database',
        #     'tags': ['mongodb', 'database', 'NoSQL'],
        #     'viewers': 104
        # }
        _id = Mongohelper.mydatabase['company_names'].insert_one(data)
        print('id=',_id.inserted_id)
        return str(_id.inserted_id)

    def readdb(self,_id):
        cursor = [i for i in Mongohelper.mydatabase['company_names'].find({"_id": ObjectId(_id)})]
        print(type(cursor))
        print(cursor)
        # for record in cursor:
        #     print(record)
        data = json.dumps(cursor, indent=4, default=json_util.default)
        print("data=",data)
        return data


if __name__ == "__main__":
    db = Mongohelper()
    # _id=db.insert_doc()
    # db.readdb(_id)



