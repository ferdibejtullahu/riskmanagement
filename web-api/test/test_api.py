
import json
from .base import BaseTestCase


class FlaskTestCase(BaseTestCase):
# Users
    def test_users_create(self):
        rv = self.post_json('/users', {
            'name': 'new test user'
        })
        res = rv.json
        self.assertEqual(res['name'], "new test user")

    def test_users_get_all(self):
        rv = self.client.get('/users')
        self.assertEqual(len(rv.json), 1)

    def test_users_get_by_id(self):
        rv = self.client.get('/users/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_users_update(self):
        rv = self.put_json('/users/1', {
            'name': 'update test user'
        })
        res = rv.json
        self.assertEqual(res['name'], "update test user")

    def test_users_delete(self):
        rv = self.client.delete('/users/1')
        res = rv.json
        self.assertEqual(res['name'], "test name")
# Risk
    def test_risk_create(self):
        rv = self.post_json('/risks', {
            'name': 'new test risk'
        })
        res = rv.json
        self.assertEqual(res['name'], "new test risk")
      
    def test_risk_get_all(self):
        rv = self.client.get('/risks')
        self.assertEqual(len(rv.json), 1)

    def test_risk_get_by_id(self):
        rv = self.client.get('/risks/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_risk_update(self):
        rv = self.put_json('/risks/1', {
            'name': 'update test risk'
        })
        res = rv.json
        self.assertEqual(res['name'], "update test risk")

    def test_risk_delete(self):
        rv = self.client.delete('/risks/1')
        res = rv.json
        self.assertEqual(res['name'], "test name")
# Risk value
    def test_risk_value_create(self):
        rv = self.post_json('/riskvalues', {
            'code': 'new test code'
        })
        res = rv.json
        self.assertEqual(res['code'], "new test code")
      
    def test_risk_value_get_all(self):
        rv = self.client.get('/riskvalues')
        self.assertEqual(len(rv.json), 1)

    def test_risk_value_get_by_id(self):
        rv = self.client.get('/riskvalues/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_risk_value_update(self):
        rv = self.put_json('/riskvalues/1', {
            'code': 'update test code'
        })
        res = rv.json
        self.assertEqual(res['code'], "update test code")

    def test_risk_value_delete(self):
        rv = self.client.delete('/riskvalues/1')
        res = rv.json
        self.assertEqual(res['code'], "test unique code")
# Property value
    def test_property_value_create(self):
        rv = self.post_json('/propertyvalues', {
            'value': 'new test value',
            'property_id': 1,
            'risk_value_id': 1
        })
        res = rv.json
        self.assertEqual(res['value'], "new test value")
      
    def test_property_value_get_all(self):
        rv = self.client.get('/propertyvalues')
        self.assertEqual(len(rv.json), 1)

    def test_property_value_get_by_id(self):
        rv = self.client.get('/propertyvalues/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_property_value_update(self):
        rv = self.put_json('/propertyvalues/1', {
            'value': 'update test value',
            'property_id': 1,
            'risk_value_id': 1
        })
        res = rv.json
        self.assertEqual(res['value'], "update test value")

    def test_property_value_delete(self):
        rv = self.client.delete('/propertyvalues/1')
        res = rv.json
        self.assertEqual(res['value'], "test value")
# Property type
    def test_property_type_create(self):
        rv = self.post_json('/propertytypes', {
            'name': 'new test name'
        })
        res = rv.json
        self.assertEqual(res['name'], "new test name")
      
    def test_property_type_get_all(self):
        rv = self.client.get('/propertytypes')
        self.assertEqual(len(rv.json), 1)

    def test_property_type_get_by_id(self):
        rv = self.client.get('/propertytypes/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_property_type_update(self):
        rv = self.put_json('/propertytypes/1', {
            'name': 'update test name'
        })
        res = rv.json
        self.assertEqual(res['name'], "update test name")

    def test_property_type_delete(self):
        rv = self.client.delete('/propertytypes/1')
        res = rv.json
        self.assertEqual(res['name'], "test name")
# Property option
    def test_property_option_create(self):
        rv = self.post_json('/propertyoptions', {
            'name': 'new test name',
            'property_id':1
        })
        res = rv.json
        self.assertEqual(res['name'], "new test name")
      
    def test_property_option_get_all(self):
        rv = self.client.get('/propertyoptions')
        self.assertEqual(len(rv.json), 1)

    def test_property_option_get_by_id(self):
        rv = self.client.get('/propertyoptions/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_property_option_update(self):
        rv = self.put_json('/propertyoptions/1', {
            'name': 'update test name',
            'property_id':1
        })
        res = rv.json
        self.assertEqual(res['name'], "update test name")

    def test_property_option_delete(self):
        rv = self.client.delete('/propertyoptions/1')
        res = rv.json
        self.assertEqual(res['name'], "test name")
# Property
    def test_property_create(self):
        rv = self.post_json('/properties', {
            'name': 'new test name',
            'caption': 'new test caption',
            'display': True,
            'risk_id':1,
            'property_type_id':1
        })
        res = rv.json
        self.assertEqual(res['name'], "new test name")
      
    def test_property_get_all(self):
        rv = self.client.get('/properties')
        self.assertEqual(len(rv.json), 1)

    def test_property_get_by_id(self):
        rv = self.client.get('/properties/1')
        res = rv.json
        self.assertEqual(res['id'], 1)

    def test_property_update(self):
        rv = self.put_json('/properties/1', {
            'name': 'update test name',
            'caption': 'new test caption',
            'display': True,
            'risk_id':1,
            'property_type_id':1
        })
        res = rv.json
        self.assertEqual(res['name'], "update test name")

    def test_property_delete(self):
        rv = self.client.delete('/properties/1')
        res = rv.json
        self.assertEqual(res['name'], "test name")
