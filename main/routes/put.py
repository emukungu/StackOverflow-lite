from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>/answers/<int:answerId>', methods = ['PUT'])
@jwt_required
def update_an_answer(questionId, answerId = None):
    """ The answer author will update his answer using this endpoint"""

    current_user_id  = get_jwt_identity()["user_id"]
    data = request.get_json()
    qn_answer = data["answer"]

    cur.execute("SELECT answer FROM answers WHERE question_id = %s AND user_id = %s; ", (questionId, current_user_id))
    queried_answer = cur.fetchone()[0]
    print(queried_answer)
    # for row in queried_answer:
        
    if not queried_answer:
        return jsonify({"message":"Your answer does not exist"}), 401

    cur.execute("UPDATE answers SET answer = %s WHERE answer = %s; ", (qn_answer, queried_answer))
    conn.commit()
    return jsonify({"message":"Your answer has been updated"})
    