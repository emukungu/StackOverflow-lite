from .baseRoutes import *

@app.route('/api/v1/questions/<int:questionId>', methods = ['GET'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    print(questions_list)
    for question in questions_list:
        print(question.question_id()," ", questionId)
        if  questionId == question.question_id():
            question_details = question.question_details()        
            return jsonify(question_details), 200 
           
    message = {"message": "The question doesnot exist on this platform"}
    return message["message"], 404
