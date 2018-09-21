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
                return jsonify({"Successful":"Your answer has been added", "QuestionId":questionId}), 201      
        return jsonify({"message": "Question doesnot exist"}), 404    

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/answers', methods= ['GET'])
def get_all_answers():
    """ This endpoint will reject returning all answers on the platform"""
    return jsonify({"message":"Please enter the correct URL method"}), 405