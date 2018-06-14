
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.user import User, UserDto

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('', methods=['GET'])
def get_all():
    users = User.query.all()
    user_dto = UserDto(many=True)
    output = user_dto.dump(users).data
    return jsonify(output)


@user_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    user = User.query.get(id)
    if not user:
        return jsonify('no record found')

    user_dto = UserDto()
    output = user_dto.dump(user).data
    return jsonify(output)


@user_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    user = User(name=data['name'])
    db.session.add(user)
    db.session.commit()
    
    user_dto = UserDto()
    output = user_dto.dump(user).data
    return jsonify(output)


@user_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify('no record found')
    user.name = data['name']
    db.session.commit()
     
    user_dto = UserDto()
    output = user_dto.dump(user).data
    return jsonify(output)   


@user_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.get(id)
    if not user:
        return jsonify('no record found')
    db.session.delete(user)
    db.session.commit()

    user_dto = UserDto()
    output = user_dto.dump(user).data
    return jsonify(output)   
    
