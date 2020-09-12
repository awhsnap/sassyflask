from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PleaseLogin(Resource):
    def get(self):
        return {"data": "Please Login"}

api.add_resource(PleaseLogin, "/")


if __name__ == "__main__":
    app.run(debug=True)