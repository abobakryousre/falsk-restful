from flask_restful import Resource, reqparse, abort



exercieses_post_parser = reqparse.RequestParser()

exercieses_post_parser.add_argument('name',type=str, help="please enter exerciese name!" ,required=True)
exercieses_post_parser.add_argument('count',type=int,help="please enter exerciese count!" , required=True)
exercieses_post_parser.add_argument('description',type=str, help="please enter description for the exerciese!")



exercieses_put_parser = reqparse.RequestParser()

exercieses_put_parser.add_argument('name',type=str )
exercieses_put_parser.add_argument('count',type=int)
exercieses_put_parser.add_argument('description',type=str)
exe_list = {}

class ExerciesesList(Resource):
    def get(self):
        return {"data": exe_list}
    def post(self):
        data = exercieses_post_parser.parse_args()
        exe_list[data.get('name')] = data
        return { "data": "Excerices Created" }, 201
    

class Exercieses(Resource):

    def get(self,exerciese_name):
        return {"data": exe_list[exerciese_name]}
    
    def put(self,exerciese_name):
        # the updated data
        data = exercieses_put_parser.parse_args()
        # get exe old based on the name
        exe = exe_list[exerciese_name]
        if "name" in data:
            exe["name"] = data.get('name')

        if "count" in data:
            exe["count"] = data.get('count')
        if "description" in data:
            exe['description'] = data.get("description")
        
        return {"data": f"{exerciese_name} updated!"}, 204
    
    def delete(self,exerciese_name):
        if exe_list[exerciese_name]:
            del exe_list[exerciese_name]
            return {"data": f"{exerciese_name} deleted"}, 203