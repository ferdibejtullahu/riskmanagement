
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.property_option import PropertyOption, PropertyOptionDto

property_option_blueprint = Blueprint('property_option', __name__)

@property_option_blueprint.route('', methods=['GET'])
def get_all():
    property_options = PropertyOption.query.all()
    property_option_dto = PropertyOptionDto(many=True)
    output = property_option_dto.dump(property_options).data
    return jsonify(output)


@property_option_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    prop = PropertyOption.query.get(id)
    if not prop:
        return jsonify('no record found')

    property_option_dto = PropertyOptionDto()
    output = property_option_dto.dump(prop).data
    return jsonify(output)


@property_option_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    prop = PropertyOption(name=data['name'],property_id=data['property_id'])
    db.session.add(prop)
    db.session.commit()
    
    property_option_dto = PropertyOptionDto()
    output = property_option_dto.dump(prop).data
    return jsonify(output)


@property_option_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    prop = PropertyOption.query.get(id)
    if not prop:
        return jsonify('no record found')
    prop.name = data['name']
    prop.property_id = data['property_id']
    db.session.commit()
     
    property_option_dto = PropertyOptionDto()
    output = property_option_dto.dump(prop).data
    return jsonify(output)   


@property_option_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    prop = PropertyOption.query.get(id)
    if not prop:
        return jsonify('no record found')
    db.session.delete(prop)
    db.session.commit()

    property_option_dto = PropertyOptionDto()
    output = property_option_dto.dump(prop).data
    return jsonify(output)   
    
