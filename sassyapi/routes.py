import uuid
from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from .models import User
from .extensions import guard, db


api = Blueprint('api', __name__)

@api.route('/login')
def login():
    """
    Parse the POST request with user credentials 
    and issue JWT token for their troubles.
    """
    jdata = request.get_json()
    username = jdata['username']
    password = jdata['password']

    user = guard.authenticate(username, password)

    token = guard.encode_jwt_token(user)
    return jsonify({'access-token': token})

@api.route('/users')
def list_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['username'] = user.username
        user_data['email'] = user.email
        output.append(user_data)
    return jsonify({'users':output})

@api.route('/user/register', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_pass = guard.hash_password(data['password'])
    new_user = User(public_id=str(uuid.uuid4()), username=data['username'], email=data['email'], password=hashed_pass)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "user created"})


@api.route('/user/<public_id>', methods=['PUT'])
def upgrade_user(public_id):
    user = User.query.filter_by(public_id)

@api.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    user = User.query.filter_by(public_id)

@api.route('/dashboard')
@auth_required
def protected():
    
    return jsonify({"data": "Special Area"})