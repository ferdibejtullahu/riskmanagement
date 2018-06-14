from app import db, ma

class Risk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    properties = db.relationship('Property', backref='risk')
    
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Risk %r>' % (self.name)

class RiskDto(ma.ModelSchema):
    class Meta:
        model = Risk