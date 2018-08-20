from flask import Flask
from routes.routes import post, get_all_questions, question_id, answer

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)