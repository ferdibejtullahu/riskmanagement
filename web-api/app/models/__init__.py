# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Define database
db = SQLAlchemy()

# Define the mashmallow serializer
ma = Marshmallow()