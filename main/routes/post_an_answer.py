from .baseRoutes import request, jsonify, json, status, app, Answer, cur,conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>/answers', methods= ['POST'])
@jwt_required
def answers(questionId):
    """This endpoint will post an answer to a specific question """
    current_user_id = get_jwt_identity()["user_id"]
    answer_data = request.get_json()

    if not answer_data:
        return jsonify({"error":"Invalid inputs"}), 400

    qn_answer = answer_data['answer']

    user_id = current_user_id     

    if type(qn_answer) is not str or type(user_id) is not int:
        return jsonify({"error":"Enter the correct values"}), 400  

    if qn_answer and user_id:
        cur.execute("SELECT question_id FROM questions WHERE question_id = %s;", (questionId,))
        qn_to_be_answered = cur.fetchall()

        for row in qn_to_be_answered:     
            if row[0] == questionId:
                cur.execute("SELECT answer FROM answers WHERE question_id = %s;", (questionId,))
                repeated_answer = cur.fetchall()

                for row in repeated_answer:
                    if row[0] == qn_answer:
                        return jsonify({"message":"Answer already exists"}), 400
                        
                query = "INSERT INTO answers (answer, question_id, user_id) VALUES(%s, %s, %s);"
                cur.execute(query, (qn_answer, questionId, user_id))
                conn.commit()
                cur.execute(""" SELECT users.username, answers.answer, answers.answer_id
                    FROM answers
                    INNER JOIN users
                    ON answers.user_id = users.user_id
                    WHERE answers.answer = %s 
                    AND answers.question_id = %s 
                    AND answers.user_id = %s; """,
                    (qn_answer, questionId, user_id))
                queried_answer = cur.fetchone()
                posted_answer = {
                    "username":queried_answer[0],
                    "answer":queried_answer[1],
                    "ans_id":queried_answer[2]
                }

                return jsonify({"message":"Your answer has been added", "Results":posted_answer}), 201      
        return jsonify({"message": "Question doesnot exist"}), 404    

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/questions/<int:questionId>/answers', methods= ['GET'])
def get_all_answers(questionId):
    """ This endpoint will get answers to a specific question"""
    all_answers = []
    cur.execute("""SELECT users.username, answers.answer, answers.answer_id
                FROM answers
                INNER JOIN users
                ON answers.user_id = users.user_id
                WHERE answers.question_id = %s""", (questionId,))
    returned_all_answers = cur.fetchall()

    if not returned_all_answers:
        return jsonify({"message":"No answers exist for the question."}), 404

    for row in returned_all_answers:                          
        returned_ans = {
            "answered_user": row[0],
            "answer":row[1],
            "ans_id":row[2]
        }
        all_answers.append(returned_ans)
    return jsonify({"Results": all_answers}), 200


