from flask import Flask, request, jsonify
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):
        data = request.get_json()
        x  = data["x"]
        y = data["y"]
        z = x+y
        retJson = {
            "Massage":z,
            "Status":200
        }
        return jsonify(retJson)
    
api.add_resource(Add, "/add")

@app.route("/k", methods = ["POST", "GET"])
def func():
    if request.method == "GET":
        data = {
            "Name":"Itech",
            "Branch":"Nerul"
        }
    else:
        data = request.get_json()
        print(data)
    return data

if __name__=="__main__":
    app.run(debug = True)