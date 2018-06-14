
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.risk_value import RiskValue, RiskValueDto

risk_value_blueprint = Blueprint('risk_values', __name__)

@risk_value_blueprint.route('', methods=['GET'])
def get_all():
    risk_values = RiskValue.query.all()
    risk_value_dto = RiskValueDto(many=True)
    output = risk_value_dto.dump(risk_values).data
    return jsonify(output)


@risk_value_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    risk_value = RiskValue.query.get(id)
    if not risk_value:
        return jsonify('no record found')

    risk_value_dto = RiskValueDto()
    output = risk_value_dto.dump(risk_value).data
    return jsonify(output)


@risk_value_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    risk_value = RiskValue(code=data['code'])
    db.session.add(risk_value)
    db.session.commit()
    
    risk_value_dto = RiskValueDto()
    output = risk_value_dto.dump(risk_value).data
    return jsonify(output)


@risk_value_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    risk_value = RiskValue.query.get(id)
    if not risk_value:
        return jsonify('no record found')
    risk_value.code = data['code']
    db.session.commit()
     
    risk_value_dto = RiskValueDto()
    output = risk_value_dto.dump(risk_value).data
    return jsonify(output)   


@risk_value_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    risk_value = RiskValue.query.get(id)
    if not risk_value:
        return jsonify('no record found')
    db.session.delete(risk_value)
    db.session.commit()

    risk_value_dto = RiskValueDto()
    output = risk_value_dto.dump(risk_value).data
    return jsonify(output)   
    
