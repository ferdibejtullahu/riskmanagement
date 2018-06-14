# Import flask
import os
from flask import Flask
from config import Development, Production
from app.models import db, ma
from flask_cors import CORS

# Define the WSGI application object
app = Flask(__name__)
CORS(app)
# Configurations
if os.environ.get('FLASK_PRODUCTION'):
    app.config.from_object(Production)
else:
    app.config.from_object(Development)

# Define the database object which is imported
db.init_app(app)
ma.init_app(app)

# Build the database:
# This will create the database file using SQLAlchemy
with app.app_context():
    from app.models.user import User 
    from app.models.property_option import PropertyOption
    from app.models.property_value import PropertyValue
    from app.models.property import Property 
    from app.models.property_type import PropertyType     
    from app.models.risk import Risk    
    from app.models.risk_value import RiskValue
    
    # This should work because we are in an app context.
    db.create_all()



# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.controllers.main_api import main_blueprint
from app.controllers.user_api import user_blueprint
from app.controllers.property_type_api import property_type_blueprint
from app.controllers.property_api import property_blueprint
from app.controllers.risk_api import risk_blueprint
from app.controllers.property_option_api import property_option_blueprint
from app.controllers.property_value_api import property_value_blueprint
from app.controllers.risk_value_api import risk_value_blueprint
# Register blueprint(s)

app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(property_type_blueprint, url_prefix='/propertytypes')
app.register_blueprint(property_blueprint, url_prefix='/properties')
app.register_blueprint(risk_blueprint, url_prefix='/risks')
app.register_blueprint(property_option_blueprint, url_prefix='/propertyoptions')
app.register_blueprint(property_value_blueprint, url_prefix='/propertyvalues')
app.register_blueprint(risk_value_blueprint, url_prefix='/riskvalues')

