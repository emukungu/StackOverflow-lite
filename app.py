from web_app import app
from routes.routes import post, get_all_questions, question_id


if __name__ == '__main__':
    app.run(debug=True)