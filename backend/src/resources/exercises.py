from flask_restful import Resource



class Exercieses(Resource):
    def get(self):
        return {"data": "empty resourece"}
    def post(self):
        return {"data": "exerciese created"}