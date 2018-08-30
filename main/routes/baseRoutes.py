from flask import request, jsonify, json
from ..models.question_model import Question
from ..models.answer_model import Answer
from ..models.user_model import User
from flask_api import status
from main import app
from datetime import date
from .. import create_connection
select = create_connection.query_database()
cur = select["cursor"]
conn = select["connect"]


questions_list = []
answers_list = []