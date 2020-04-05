from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from validate import validateUser
from model import call_model

app = Flask(__name__)
api = Api(app)


class Compare(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        validated = validateUser(username, password)
        if validated:
            model_output = call_model(data['content'])
        response = {
            "status": 200,
            "result": model_output
        }
        return jsonify(response)

api.add_resource(Compare, '/compare')

if __name__ == "__main__":
    # TODO: update host to work with the container
    app.run()