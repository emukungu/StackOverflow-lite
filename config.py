import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'bootcamp'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    
class ProductionConfig(Config):
    DEBUG = False
    
    
class TestingConfig(Config):
    DEBUG = True
    
   
    