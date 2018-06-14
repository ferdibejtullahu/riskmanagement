
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.property_type import PropertyType, PropertyTypeDto

property_type_blueprint = Blueprint('property_type', __name__)

@property_type_blueprint.route('', methods=['GET'])
def get_all():
    property_types = PropertyType.query.all()
    property_type_dto = PropertyTypeDto(many=True)
    output = property_type_dto.dump(property_types).data
    return jsonify(output)


@property_type_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    property_type = PropertyType.query.get(id)
    if not property_type:
        return jsonify('no record found')

    property_type_dto = PropertyTypeDto()
    output = property_type_dto.dump(property_type).data
    return jsonify(output)


@property_type_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    property_type = PropertyType(name=data['name'])
    db.session.add(property_type)
    db.session.commit()
    
    property_type_dto = PropertyTypeDto()
    output = property_type_dto.dump(property_type).data
    return jsonify(output)


@property_type_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    property_type = PropertyType.query.get(id)
    if not property_type:
        return jsonify('no record found')
    property_type.name = data['name']
    db.session.commit()
     
    property_type_dto = PropertyTypeDto()
    output = property_type_dto.dump(property_type).data
    return jsonify(output)   


@property_type_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    property_type = PropertyType.query.get(id)
    if not property_type:
        return jsonify('no record found')
    db.session.delete(property_type)
    db.session.commit()

    property_type_dto = PropertyTypeDto()
    output = property_type_dto.dump(property_type).data
    return jsonify(output)   
    
