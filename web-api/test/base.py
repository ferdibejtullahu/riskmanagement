from flask_testing import TestCase
from app import app, db
from app.models.user import User
from app.models.property_type import PropertyType
from app.models.property_option import PropertyOption
from app.models.property import Property
from app.models.property_value import PropertyValue
from app.models.risk import Risk
from app.models.risk_value import RiskValue
from config import Testing
import json

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(Testing)
        return app

    def setUp(self):
        self.create_database()

    def tearDown(self):
        pass

    def post_json(self, url, json_dict):
        """Send dictionary json_dict as a json to the specified url """
        return self.client.post(url, data=json.dumps(json_dict), content_type='application/json')
    
    def put_json(self, url, json_dict):
        """Send dictionary json_dict as a json to the specified url """
        return self.client.put(url, data=json.dumps(json_dict), content_type='application/json')

    def create_database(self):
        # initialize database
        db.drop_all()
        db.create_all()

        # create use
        user = User('test name')
        db.session.add(user)

        # create property type
        property_type = PropertyType('test name')
        db.session.add(property_type)

        # create risk
        risk = Risk('test name')
        db.session.add(risk)

        # create property
        prop= Property('test name', 'test caption', risk.id, property_type.id)
        db.session.add(prop)
 
        # create property option
        property_option = PropertyOption('test name', prop.id)
        db.session.add(property_option)

        # create risk value
        risk_value = RiskValue('test name', 'test unique code')
        db.session.add(risk_value)

        # create property option
        risk_property_value = PropertyValue('test value',prop.id,risk_value.id)
        db.session.add(risk_property_value)

        #commit changes        
        db.session.commit()