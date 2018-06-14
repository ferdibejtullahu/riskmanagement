
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.property_value import PropertyValue, PropertyValueDto

property_value_blueprint = Blueprint('property_value', __name__)

@property_value_blueprint.route('', methods=['GET'])
def get_all():
    property_values = PropertyValue.query.all()
    property_value_dto = PropertyValueDto(many=True)
    output = property_value_dto.dump(property_values).data
    return jsonify(output)


@property_value_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    prop = PropertyValue.query.get(id)
    if not prop:
        return jsonify('no record found')

    property_value_dto = PropertyValueDto()
    output = property_value_dto.dump(prop).data
    return jsonify(output)


@property_value_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    prop = PropertyValue(value=data['value'],property_id=data['property_id'],risk_value_id=data['risk_value_id'])
    db.session.add(prop)
    db.session.commit()
    
    property_value_dto = PropertyValueDto()
    output = property_value_dto.dump(prop).data
    return jsonify(output)


@property_value_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    prop = PropertyValue.query.get(id)
    if not prop:
        return jsonify('no record found')
    prop.value = data['value']
    prop.property_id = data['property_id']
    prop.risk_value_id = data['risk_value_id']
    db.session.commit()
     
    property_value_dto = PropertyValueDto()
    output = property_value_dto.dump(prop).data
    return jsonify(output)   


@property_value_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    prop = PropertyValue.query.get(id)
    if not prop:
        return jsonify('no record found')
    db.session.delete(prop)
    db.session.commit()

    property_value_dto = PropertyValueDto()
    output = property_value_dto.dump(prop).data
    return jsonify(output)   
    
