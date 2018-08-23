from flask import request, jsonify, json
from copy import deepcopy
from ..models.question_model import Question
from ..models.answer_model import Answer
from flask_api import status
from main import app
from datetime import date

questions_list = []
answers_list = []