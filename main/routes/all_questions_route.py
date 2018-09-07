from .baseRoutes import request, jsonify, status, app, questions_list


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    listed_questions = []
    if questions_list == []:
        return jsonify({"message":"No questions exist on this platform"}), 404
    for question in questions_list:
        #return dictionary that can be jsonified easily
        questions = question.listed_question()  
        listed_questions.append(questions)
    return jsonify(listed_questions), 200
