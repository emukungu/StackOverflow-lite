import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'bootcamp'
    DATABASE_URI = os.environ.get('DATABASE_URL')
    

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT= True
    DATABASE_URI = 'postgres://localhost/crud'
    
class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True  
    DATABASE = 'host' 

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'postgres://localhost/test'
    
    