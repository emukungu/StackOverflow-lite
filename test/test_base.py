import unittest
from flask_api import status
from main import app
from flask import json

class TestBase(unittest.TestCase):
    """ set up a client for the app"""
    def setUp(self):
        self.app = app.test_client()