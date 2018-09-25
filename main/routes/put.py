from .baseRoutes import request, jsonify, json, status, Question, app, date, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>/answers/<int:answerId>', methods = ['PUT'])
@jwt_required
def update_an_answer(questionId, answerId):
    """ The answer author will update his answer using this endpoint"""

    current_user_id  = get_jwt_identity()["user_id"]
    
    # updating answerer
    cur.execute("SELECT answer FROM answers WHERE answer_id = %s AND user_id = %s; ", (answerId, current_user_id))
    queried_answer = cur.fetchone()

    # voting prefered answer; author
    cur.execute("SELECT question_id FROM questions WHERE question_id = %s AND user_id = %s",(questionId, current_user_id))
    qn_answer_preferred = cur.fetchone()   
            
    if queried_answer:
        data = request.get_json()
        qn_answer = data["answer"]
        if not qn_answer:
         return jsonify({"message":"Fill in the missing fields"}), 400
        cur.execute("SELECT answer FROM answers WHERE answer = %s AND question_id =%s;", (qn_answer, questionId))
        res = cur.fetchone()
        if not res:
            query = "UPDATE answers SET answer = %s WHERE answer = %s AND answer_id = %s; "
            cur.execute(query,(qn_answer, queried_answer, answerId))
            conn.commit()
            return jsonify({"message":"Your answer has been updated"}), 200
        return jsonify({"message":"Answer for the question already exists"}), 403

    elif qn_answer_preferred:
        cur.execute("SELECT answer FROM answers WHERE question_id = %s",(questionId,))
        preferred_answer = cur.fetchall()
        return jsonify({"message":"Author's preferred answer "+ preferred_answer})

    elif not queried_answer:
        return jsonify({"message":"You don't have editing priviledges for this question"}), 403
    elif not qn_answer_preferred:
        return jsonify({"message":"You don't priviledges to prefer this answer"}), 403
    