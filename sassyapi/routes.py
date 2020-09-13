from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from .extensions import guard

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']

    user = guard.authenticate(username, password)
    token = guard.encode_jwt_token(user)
    return jsonify({'access-token': token})

@api.route('/dashboard', methods=['GET'])
@auth_required
def protected():
    return {'Special Area'}