from app import db, ma

class PropertyValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(150), unique=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    risk_value_id = db.Column(db.Integer, db.ForeignKey('risk_value.id'))
    
    def __init__(self, value=None, property_id=None, risk_value_id=None):
        self.value = value
        self.property_id = property_id
        self.risk_value_id = risk_value_id


    def __repr__(self):
        return '<PropertyValue %r>' % (self.name)

class PropertyValueDto(ma.ModelSchema):
    class Meta:
        model = PropertyValue


