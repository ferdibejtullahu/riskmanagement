from app import db, ma

class PropertyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    properties = db.relationship('Property', backref='property_type')
    
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<PropertyType %r>' % (self.name)

class PropertyTypeDto(ma.ModelSchema):
    class Meta:
        model = PropertyType


