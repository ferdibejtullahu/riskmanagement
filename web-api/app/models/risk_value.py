from app import db, ma

class RiskValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(150), unique=True)
    property_values = db.relationship('PropertyValue', backref='riskvalue')
    
    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code

    def __repr__(self):
        return '<RiskValue %r>' % (self.name)

class RiskValueDto(ma.ModelSchema):
    class Meta:
        model = RiskValue


