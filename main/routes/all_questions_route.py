from .baseRoutes import *


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    listed_questions = []
    if questions_list == []:
        message = {"message":"No questions exist on this platform"}
        return message["message"], 200
    else:
        for question in questions_list:
        #return dictionary that can be jsonified easily
            questions = question.listed_question()  
            listed_questions.append(questions)
        return jsonify(listed_questions), 200
