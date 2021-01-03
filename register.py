import sqlite3

from flask_restful import Resource, reqparse

from user import User


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):
            return "", 409

        connection = sqlite3.connect("data.db")

        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (NULL, ?, ?)",
            (data["username"], data["password"]),
        )
        connection.commit()

        connection.close()

        return "", 201
