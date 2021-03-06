from flask import Flask
import os
import psycopg2
import connexion
from flask_cors import CORS


# app = connexion.FlaskApp(__name__, specification_dir = 'swagger/')
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

CORS(app)

from .db import *


class Create_connection:
    def __init__(self):
        if os.getenv('FLASK_ENV') == 'production':
            self.con = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode = 'disable')
        else:
            self.con = psycopg2.connect(host="localhost", database="crud", user='postgres')
        self.cursor = self.con.cursor()
        self.cursor.execute(user)     
        self.cursor.execute(question)
        self.cursor.execute(answer)
        # self.cursor.execute(comment)
        # self.cursor.execute(vote)
        self.con.commit()

    def query_database(self):
        self.selector = {"cursor": self.cursor,
                         "connect": self.con
                        }
        return self.selector 


create_connection = Create_connection()

signature = app.config["SECRET_KEY"] = "bootcamp"
# app.add_api('swagger.yml')


from .routes.post_a_question_route import post_a_question
from .routes.all_questions_route import get_all_questions
from .routes.get_specific_question import question_id, wrong_qn_id
from .routes.post_an_answer import answers, get_all_answers
from .routes.signup import signup, get_all_users
from .routes.login import login, wrong_login_method
from .routes.delete import delete_question
from .routes.put import update_an_answer
from .routes.upvote_downvote import vote
from .routes.all_questions_user_asked import user_questions
from .routes.answer_comment import comment, get_all_comments
from .routes.qns_withmost_answers import qns_withmost_answers
from .routes.logout import logout
