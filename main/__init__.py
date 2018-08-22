from flask import Flask


app = Flask(__name__)

from .routes.routes import post, get_all_questions, question_id, answer
