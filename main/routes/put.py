from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date, cur, conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>/answers/<int:answerId>', methods = ['PUT'])
@jwt_required
def update_an_answer(questionId, answerId):
    """ The answer author will update his answer using this endpoint"""

    current_user_id  = get_jwt_identity()["user_id"]
    
    # updating answerer
    cur.execute("SELECT answer FROM answers WHERE answer_id = %s AND user_id = %s; ", (answerId, current_user_id))
    queried_answer = cur.fetchone()[0]

    # voting author
    cur.execute("SELECT question_id FROM questions WHERE question_id = %s AND user_id = %s",(questionId, current_user_id))
    qn_answer_vote = cur.fetchone()[0]    
            
    if queried_answer:
        data = request.get_json()
        qn_answer = data["answer"]
        cur.execute("UPDATE answers SET answer = %s WHERE answer = %s; ", (qn_answer, queried_answer))
        conn.commit()
        return jsonify({"message":"Your answer has been updated"})
    elif qn_answer_vote:
        cur.execute("SELECT up_vote FROM answers WHERE question_id = %s",(questionId,))
        current_vote = cur.fetchone[0]
        current_vote +=1
        cur.execute("UPDATE answers SET up_vote = %s WHERE question_id = %s",(current_vote, questionId))
        return jsonify({"message":"Voted", "Results": current_vote})
    