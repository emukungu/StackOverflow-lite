from flask import Flask


app = Flask(__name__)

from  .routes.post_a_question_route import post
from .routes.all_questions_route import get_all_questions
from .routes.get_specific_question import question_id
