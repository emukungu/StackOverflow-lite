import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'bootcamp'
    DATABASE_URL = os.environ['DATABASE_URI']

class DevelopmentConfig(Config):
    DEBUG = True    
    DATABASE_URL = 'postgres://localhost/crud'
    FLASK_ENV = 'development'
    
class ProductionConfig(Config):
    DEBUG = False
    
    
class TestingConfig(Config):
    DEBUG = True
    DATABASE_URL = 'postgres://localhost/test'
   
    