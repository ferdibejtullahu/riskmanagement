
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.property import Property, PropertyDto

property_blueprint = Blueprint('property', __name__)

@property_blueprint.route('', methods=['GET'])
def get_all():
    propertys = Property.query.all()
    property_dto = PropertyDto(many=True)
    output = property_dto.dump(propertys).data
    return jsonify(output)


@property_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    prop = Property.query.get(id)
    if not prop:
        return jsonify('no record found')

    property_dto = PropertyDto()
    output = property_dto.dump(prop).data
    return jsonify(output)


@property_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    prop = Property(name=data['name'],caption=data['caption'], risk_id=data['risk_id'])
    db.session.add(prop)
    db.session.commit()
    
    property_dto = PropertyDto()
    output = property_dto.dump(prop).data
    return jsonify(output)


@property_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    prop = Property.query.get(id)
    if not prop:
        return jsonify('no record found')
    prop.name = data['name']
    prop.caption = data['caption']
    prop.risk_id = data['risk_id']
    db.session.commit()
     
    property_dto = PropertyDto()
    output = property_dto.dump(prop).data
    return jsonify(output)   


@property_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    prop = Property.query.get(id)
    if not prop:
        return jsonify('no record found')
    db.session.delete(prop)
    db.session.commit()

    property_dto = PropertyDto()
    output = property_dto.dump(prop).data
    return jsonify(output)   
    
