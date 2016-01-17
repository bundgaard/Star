from bson import ObjectId
from Star.user  import User
import json


class ObjectIdEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return json.JSONEncoder.default(self, o)


def encode_user(user):
    return {"_type": "user", "name": user.name, "username": user.username, "email": user.email}

def decode_user(user_document):
    assert user_document['_type'] == 'user'
    return User(user_document['name'], user_document['username'], user_document['email'])