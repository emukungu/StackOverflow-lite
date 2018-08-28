from .baseRoutes import request, jsonify, json, status, answers_list, app, Answer, questions_list

@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['POST'])
def answer(questionId):
    """This endpoint will post an answer to a specific question """
    answer_data = request.get_json()

    if not answer_data:
        return jsonify({"error":"All data is required"}), 400

    qn_answer = answer_data['answer']
<<<<<<< HEAD
    user_id = answer_data['user_id'] 
=======
    user_id = answer_data['user_id']     
>>>>>>> ft-post-a-question-159866594

    if type(qn_answer) is not str or type(user_id) is not int:
        return jsonify({"error":"Enter the correct values"}), 400  

    if qn_answer and user_id:
        for question in questions_list:
            if question.qn_id == questionId:
                answer = Answer(user_id, questionId, qn_answer)
                answers_list.append({questionId:answer.answer_per_question()})
                return jsonify({"Successful":"Your answer has been added", "Results":answers_list}), 201 
<<<<<<< HEAD
        return jsonify({"message": "Question doesnot exist"}), 404                                                   
    
    return jsonify({"message": "Fill in all the fields"}), 400



@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['GET'])
def get_question_answers(questionId):
    """ This endpoint will get the answer for a particular question"""
=======
        return jsonify({"message": "Question doesnot exist"}), 404    

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['GET'])
def get_question_answers(questionId):
    """ This endpoint will get answers to a specific question"""
>>>>>>> ft-post-a-question-159866594

    specific_question_answers = []
    if not answers_list:
        return jsonify({"message": "No answers yet"}), 404
<<<<<<< HEAD
        
=======

>>>>>>> ft-post-a-question-159866594
    for answers in answers_list:
        for k, v in answers.items():
            if k == questionId:
                specific_question_answers.append(v)
    return jsonify({k:specific_question_answers}), 200
    