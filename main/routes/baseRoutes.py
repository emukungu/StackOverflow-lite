from flask import request, jsonify, json
from copy import deepcopy
from ..models.question_model import Question
from ..models.answer_model import Answer
from flask_api import status
from main import app
from datetime import date

questions_list = []
answers_list = []

url = "http://localhost"


def error():
    if not (url + '/api/v1/questions/<int:questionId>'):
        return jsonify({"message": "Please enter the correct URL"})
