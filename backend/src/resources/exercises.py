from flask_restful import Resource



class ExerciesesList(Resource):
    def get(self):
        return {"data": "empty resourece"}
    def post(self):
        return {"data": "exerciese created"}
    

class Exercieses(Resource):

    def get(self,exerciese_id):

        return {"data": f"return {exerciese_id}"}
    
    def put(self,exerciese_id):
        return {"data": f"{exerciese_id} updated"}
    
    def delete(self,exerciese_id):
        return {"data": f"{exerciese_id} deleted"}