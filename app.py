from web_app import app
from routes.routes import post, get_all_questions, question_id, answer


if __name__ == '__main__':
    app.run(debug=True)