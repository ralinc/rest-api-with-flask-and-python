from flask import Flask, jsonify, request

stores = [
    {
        "name": "Google",
        "items": [
            {"name": "Pixel 3a", "price": 100},
        ],
    },
    {
        "name": "Apple",
        "items": [
            {"name": "iPhone SE", "price": 200},
        ],
    },
]

app = Flask(__name__)


@app.route("/stores", methods=["POST"])
def create_store():
    params = request.get_json()
    store = {"name": params["name"], "items": []}
    stores.append(store)
    return jsonify(stores), 201


@app.route("/stores", methods=["GET"])
def get_stores():
    return jsonify(stores)


@app.route("/stores/<string:name>", methods=["GET"])
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)

    return "", 404


@app.route("/stores/<string:name>/items", methods=["POST"])
def create_store_item(name):
    params = request.get_json()

    for store in stores:
        if store["name"] == name:
            item = {"name": params["name"], "price": params["price"]}
            store["items"].append(item)
            return jsonify(item), 201

    return "", 404


@app.route("/stores/<string:name>/items", methods=["GET"])
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])

    return "", 404


app.run()
