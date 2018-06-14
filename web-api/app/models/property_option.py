from app import db, ma


class PropertyOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))

    def __init__(self, name=None, property_id=None):
        self.name = name
        self.property_id = property_id

    def __repr__(self):
        return '<PropertyOption %r>' % (self.name)


class PropertyOptionDto(ma.ModelSchema):
    class Meta:
        model = PropertyOption
