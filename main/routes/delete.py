from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>', methods = ['DELETE'])
@jwt_required
def delete_question(questionId):
    current_user = get_jwt_identity()["user_id"]
    cur.execute("SELECT question_id FROM questions WHERE question_id = %s AND user_id = %s;", (questionId, current_user))
    res = cur.fetchone()[0]
    if not res:
        return jsonify({"message":"Question does not exist"})

    cur.execute("DELETE FROM answers WHERE question_id = %s;", (questionId,))
    cur.execute("DELETE FROM questions WHERE question_id = %s AND user_id = %s;", (questionId, current_user))
    
    conn.commit()
    return jsonify({"message":"Question has been deleted"})



    
