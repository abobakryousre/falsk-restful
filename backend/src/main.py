from flask import Flask
from flask_restful import Api
from resources.exercises import Exercieses
PORT = 5000

app = Flask(__name__)
api = Api(app)

api.add_resource(Exercieses,'/exercieses')

if __name__ == "__main__":
    app.run(debug=True,port=PORT)