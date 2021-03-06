from .baseRoutes import request, jsonify, json, status, Question, app, datetime, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>', methods = ['DELETE'])
@jwt_required
def delete_question(questionId):
    current_user_id = get_jwt_identity()["user_id"]
    cur.execute("SELECT question_id FROM questions WHERE question_id = %s AND user_id = %s;", (questionId, current_user_id))
    res = cur.fetchone()

    if not res:
        return jsonify({"message":"Question does not exist OR check  if this is the question you posted." }), 405 
    
    cur.execute("SELECT answer_id FROM answers WHERE question_id = %s;",(questionId,))
    answerId = cur.fetchone()
    print(answerId)
    
    if answerId is None:
        cur.execute("DELETE FROM questions WHERE question_id = %s AND user_id = %s;", (questionId, current_user_id))
    else:   
        cur.execute("DELETE FROM votes WHERE answer_id = %s;", (answerId,))
        cur.execute("DELETE FROM comments WHERE answer_id = %s;", (answerId,))
        cur.execute("DELETE FROM answers WHERE question_id = %s;", (questionId,))
        cur.execute("DELETE FROM questions WHERE question_id = %s AND user_id = %s;", (questionId, current_user_id))
    
    conn.commit()
    return jsonify({"message":"Question has been deleted"}), 204



    
