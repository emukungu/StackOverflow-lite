from .baseRoutes import *

@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['POST'])
def answer(questionId):
    """This endpoint will post an answer to a specific question """
    data = request.get_json()
    if not data:
        return jsonify({"error":"All data is required"}), 400
    qn_answer = data['answer']
    user_id = data['user_id']   
    
    if qn_answer and user_id:
        for question in questions_list:
            if question.qn_id == questionId:
                answer = Answer(user_id, questionId, qn_answer)
                {questionId:answer.answer_per_question()}
                answers_list.append({questionId:answer.answer_per_question()})
                return jsonify(answers_list) , 201                                                        
            else:
                message = {"message": "No question with that id"}
                return message["message"], 400                      
    else:
        message = {"message": "Please add an answer to the question"}
        return message["message"], 400

