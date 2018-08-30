from .baseRoutes import request, jsonify, json, status, answers_list, app, Answer, questions_list, cur,conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['POST'])
@jwt_required
def answer(questionId):
    """This endpoint will post an answer to a specific question """
    current_user_id = get_jwt_identity()["user_id"]
    print(current_user_id)
    answer_data = request.get_json()

    if not answer_data:
        return jsonify({"error":"All data is required"}), 400

    qn_answer = answer_data['answer']

    user_id = current_user_id     

    if type(qn_answer) is not str or type(user_id) is not int:
        return jsonify({"error":"Enter the correct values"}), 400  

    if qn_answer and user_id:
        cur.execute("SELECT question_id FROM questions WHERE question_id = %s;", (questionId,))
        qn_to_be_answered = cur.fetchone()[0]
        print(qn_to_be_answered)
        if qn_to_be_answered == questionId:
            query = "INSERT INTO answers (answer, question_id, user_id) VALUES(%s, %s, %s);"
            cur.execute(query, (qn_answer, qn_to_be_answered, user_id))
            conn.commit()
            return jsonify({"Successful":"Your answer has been added", "QuestionId":qn_to_be_answered}), 201 

        return jsonify({"message": "Question doesnot exist"}), 404    

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/answers', methods= ['GET'])
def get_all_answers():
    """ This endpoint will get answers to a specific question"""
    all_answers = []
    query = "SELECT * FROM answers;" 
    cur.execute(query)
    returned_all_answers = cur.fetchall()

    if not returned_all_answers:
        return jsonify({"message":"No answers exist."}) 

    for i in returned_all_answers:
        answer_object = Answer(i[1], i[2], i[0])
        answer_details = answer_object.answer_per_question()
        all_answers.append(answer_details)
    return jsonify({"Results": all_answers})
    