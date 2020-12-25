from user import User

users = [User(1, "admin", "1")]
userid_index = {user.id: user for user in users}
username_index = {user.username: user for user in users}


def authenticate(username, password):
    user = username_index.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_index.get(user_id, None)
