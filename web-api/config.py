import os

# Development configuration
class Development(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    DEBUG = True
    SECRET_KEY = 'dev'


# Production configuration
class Production(Development):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_CHARCOAL_URL')
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_TODO_SECRET_KEY')

# Test configuration
class Testing(Development):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'    
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///data_test.db'
    LIVESERVER_PORT = 3333
    LIVESERVER_TIMEOUT = 10
    DEBUG = True
    TESTING = True
