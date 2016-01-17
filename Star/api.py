from flask import Blueprint, jsonify, abort, request
from . import mongo
from flask.ext.pymongo import ASCENDING, DESCENDING
from .util import ObjectIdEncoder, ObjectId
import json

api = Blueprint('api', __name__)

"""
The following will be error handlers for HTTP codes exposed to JSON
"""


@api.errorhandler(400)
def bad_request(error):
    resp = jsonify({'error': error.description})
    return resp


@api.errorhandler(404)
def resource_not_found(error):
    resp = jsonify({'error': error.description})
    return resp


"""
The following is the API implementation
"""


# long term idea to create a class which incorporates the different HTTP states as Class methods.



# @api.route('/scientists')
# def get_all_scientists():
#    limit = request.args.get('limit')
#    s = [s for s in mongo.db.scientists.find()]
#    return json.dumps({'scientists': s}, cls=ObjectIdEncoder), 200, {'Content-Type': 'application/json'}


@api.route('/scientists', methods=['POST'])
def add_scientist():
    if not request.json and not request.json.get("name"):
        abort(400)
    result = mongo.db.scientists.insert({'name': request.json.get('name')})
    return json.dumps({'scientists': result}, cls=ObjectIdEncoder), 200, {"Content-Type": 'application/json'}


@api.route("/scientists/<ObjectId:scientist_id>", methods=['PUT'])
def update_scientist(scientist_id):
    if not request.json and not request.json.get("name"):
        abort(400)
    m = mongo.db.scientists.find_one({"_id": scientist_id})
    if m == None:
        abort(404)
    # update using the same id and a new document
    result = mongo.db.scientists.replace_one({"_id": scientist_id}, {"name": request.json.get("name")})
    return jsonify({'scientist': str(result.matched_count)})


@api.route('/scientists/', methods=['GET'], defaults={'scientist_id': None})
@api.route('/scientists/<ObjectId:scientist_id>', methods=['GET'])
def get_scientist(scientist_id):

    if scientist_id is None:
        args_sort = request.args.get('sort')
        print("Sort: ", args_sort)

        collection = mongo.db.scientists.find().sort('name', ASCENDING)
        return json.dumps({'scientists': list(collection)}, cls=ObjectIdEncoder), 200, {
            'Content-Type': 'application/json'}
    else:
        scientist = mongo.db.scientists.find_one({"_id": scientist_id})
        if scientist == None:
            abort(404)
        return json.dumps({'scientist': scientist}, cls=ObjectIdEncoder), 200, {'Content-Type': 'application/json'}


@api.route('/scientists/<string:scientist_id>', methods=['DELETE'])
def delete_scientist(scientist_id):
    scientist = mongo.db.scientists.find_one({"_id": ObjectId(scientist_id)})
    if scientist == None:
        abort(404)
    result = mongo.db.scientists.delete_one(scientist)
    return json.dumps({'scientist': str(result.deleted_count)}), 200, {'Content-Type': 'application/json'}
