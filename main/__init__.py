from flask import Flask
import psycopg2
# from . import config


app = Flask(__name__)


from .db import *

class Create_connection:
    def __init__(self):
        self.con = psycopg2.connect(host="localhost", database="stack", user="postgres", password="postgres")
        self.cursor = self.con.cursor()
        self.cursor.execute(user)     
        self.cursor.execute(question)
        self.cursor.execute(answer)
        self.con.commit()

    def query_database(self):
        self.selector = {"cursor": self.cursor,
                         "connect": self.con
                        }
        return self.selector 


create_connection = Create_connection()


from .routes.post_a_question_route import post
from .routes.all_questions_route import get_all_questions
from .routes.get_specific_question import question_id
from .routes.post_an_answer import answer
from .routes.signup import register, get_all_users
from .routes.login import wrong_login_method
from .routes.login import login

