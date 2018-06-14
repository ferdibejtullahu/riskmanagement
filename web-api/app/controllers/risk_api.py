
from app import app, db
from flask import Blueprint, request, jsonify
from app.models.risk import Risk, RiskDto

risk_blueprint = Blueprint('risks', __name__)

@risk_blueprint.route('', methods=['GET'])
def get_all():
    risks = Risk.query.all()
    risk_dto = RiskDto(many=True)
    output = risk_dto.dump(risks).data
    return jsonify(output)


@risk_blueprint.route('/<id>', methods=['GET'])
def get_by_id(id):
    risk = Risk.query.get(id)
    if not risk:
        return jsonify('no record found')

    risk_dto = RiskDto()
    output = risk_dto.dump(risk).data
    return jsonify(output)


@risk_blueprint.route('', methods=['POST'])
def create():
    data = request.get_json()
    risk = Risk(name=data['name'])
    db.session.add(risk)
    db.session.commit()
    
    risk_dto = RiskDto()
    output = risk_dto.dump(risk).data
    return jsonify(output)


@risk_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    risk = Risk.query.get(id)
    if not risk:
        return jsonify('no record found')
    risk.name = data['name']
    db.session.commit()
     
    risk_dto = RiskDto()
    output = risk_dto.dump(risk).data
    return jsonify(output)   


@risk_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    risk = Risk.query.get(id)
    if not risk:
        return jsonify('no record found')
    db.session.delete(risk)
    db.session.commit()

    risk_dto = RiskDto()
    output = risk_dto.dump(risk).data
    return jsonify(output)   
    
