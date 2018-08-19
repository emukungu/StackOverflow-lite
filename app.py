from web_app import app
from routes.routes import post, get_all_questions


if __name__ == '__main__':
    app.run(debug=True)