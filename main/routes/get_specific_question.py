from .baseRoutes import request, jsonify, json, status, app, questions_list, url, error

@app.route('/api/v1/questions/<int:questionId>', methods = ['GET', 'POST'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    if request.method == 'GET':
        for question in questions_list:
            if  questionId == question.question_id():
                question_details = question.question_details()        
                return jsonify(question_details), 200 
        return jsonify({"message": "The question doesnot exist on this platform"}), 404

    elif request.method == 'POST':
        return jsonify({"message":"Please enter the correct URL method"}), 404
