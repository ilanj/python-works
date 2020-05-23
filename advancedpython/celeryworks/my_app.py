import celery
from flask import Flask, app
from flask_restful import Api, Resource
import time
import threading

app = Flask(__name__)
api = Api(app)


class Main(Resource):

    def get(self):
        task.delay()
        return "demo of celery"

api.add_resource(Main, '/')

if __name__ == "__main__":
    app.run(debug=True)

