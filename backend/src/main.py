from flask import Flask
from flask_restful import Api
from resources.exercises import ExerciesesList, Exercieses
PORT = 5000

app = Flask(__name__)
api = Api(app)

api.add_resource(ExerciesesList,'/exercieses')
api.add_resource(Exercieses,'/exercieses/<int:exerciese_id>')

if __name__ == "__main__":
    app.run(debug=True,port=PORT)