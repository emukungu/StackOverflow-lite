import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'bootcamp'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'host="localhost", database="crud", user="postgres", password="postgres"'
    ENV = "development"
    
class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'host_crud'
    ENV = "production"

class TestingConfig(Config):
    DEBUG = True
    DATABASE_URI = 'test_db'
    ENV = "testing"