from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource

from security import authenticate, identity

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return item if item else "", 404

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return "", 200

    @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x["name"] == params["name"], items), None)
        if not item:
            return "", 404

        params = request.get_json()
        item["price"] = params["price"]
        return item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return items

    @jwt_required()
    def post(self):
        params = request.get_json()

        if next(filter(lambda x: x["name"] == params["name"], items), None):
            return "", 409

        item = {"name": params["name"], "price": params["price"]}
        items.append(item)
        return item, 201


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "dummy"

jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(ItemList, "/items")
api.add_resource(Item, "/items/<string:name>")

app.run()
