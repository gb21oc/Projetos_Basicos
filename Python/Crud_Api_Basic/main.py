from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)



# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    app.run(debug=True)



