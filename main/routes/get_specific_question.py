from .baseRoutes import request, jsonify, json, status, app, questions_list, date

@app.route('/api/v1/questions/<int:questionId>', methods = ['GET'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    for question in questions_list:
        if  questionId == question.question_id():
            question_details = question.question_details()        
            return jsonify(question_details), 200 
    return jsonify({"message": "The question doesnot exist on this platform"}), 404
