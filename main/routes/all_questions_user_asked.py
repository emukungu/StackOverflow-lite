from .baseRoutes import request, jsonify, json, status, Question, app, date, cur, conn
from .login import jwt_required, get_jwt_identity, login


@app.route('/api/v1/user/questions', methods= ['GET'])
@jwt_required
def user_questions():
    """ This endpoint will get questions by a specific user"""
    current_user_id = get_jwt_identity()["user_id"]
    userId = current_user_id

    user_question = []
    cur.execute(""" SELECT users.username, questions.title, questions.date_created, questions.question_id
                    FROM questions
                    INNER JOIN users
                    ON questions.user_id = users.user_id
                    WHERE users.user_id = %s
                    ORDER BY questions.date_created DESC;""",(userId,))
    returned_user_questions = cur.fetchall()

    if not returned_user_questions:
        return jsonify({"message":"You have not posted any questions."}), 404 
    for row in returned_user_questions:
        returned_object = {
        "username": row[0],
        "title": row[1],
        "date_created": row[2],
        "qn_id": row[3]
        }    
        user_question.append(returned_object)

    return jsonify({"message":"Successfully returned all user questions","Results": user_question}), 200

