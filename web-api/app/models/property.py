from app import db, ma

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    risk_id = db.Column(db.Integer, db.ForeignKey('risk.id'))
    property_type_id = db.Column(db.Integer, db.ForeignKey('property_type.id'))
    name = db.Column(db.String(150), unique=True)
    caption = db.Column(db.String(150))
    display = db.Column(db.Boolean)
    property_options = db.relationship('PropertyOption', backref='property')
    property_values = db.relationship('PropertyValue', backref='property')
    
    def __init__(self, name=None, caption=None, risk_id=None, property_type_id=None):
        self.name = name
        self.caption = caption
        self.risk_id = risk_id
        self.property_type_id = property_type_id

    def __repr__(self):
        return '<Property %r>' % (self.name)

class PropertyDto(ma.ModelSchema):
    class Meta:
        model = Property