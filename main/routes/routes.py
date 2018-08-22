from flask import request, jsonify, json
from copy import deepcopy
from ..models.question_model import Question
from ..models.answer_model import Answer
from flask_api import status
from main import app

questions_list = []
answers_list = []

@app.route('/api/v1/questions', methods = ['POST'])
def post():
    """This endpoint will post a question """
    message = {"message":""}
    if request.method == 'POST':        
        #data from the client
        data = request.json
        title= data['title']
        desc = data['description']
        date= data['date']
        user_id = data['user_id']
        if title == "" or desc == "" or date == "":
            message["message"] = "Fill in all the fields "
            return message["message"], 400
        else:
            #create an object from it
            question =  Question(title, desc, user_id, date)
            # store the object in a list
            questions_list.append(question)
            message = {"message":"Your question has been posted"}

            return message["message"], 200               


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    listed_questions = []
    if questions_list == []:
        message = {"message":"No questions exist on this platform"}
        return message["message"], 404
    else:
        for question in questions_list:
        #return dictionary that can be jsonified easily
            questions = question.listed_question()  
            listed_questions.append(questions)
        return jsonify(listed_questions), 200


@app.route('/api/v1/questions/<int:questionId>', methods = ['GET'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    for question in questions_list:
        if  questionId == question.question_id():
            question_details = question.question_details()        
            return jsonify(question_details), 200
        else:         
            message = {"message": "The question doesnot exist on this platform"}
            return message["message"], 404


@app.route('/api/v1/questions/<int:questionId>/answer', methods= ['POST'])
def answer(questionId):
    """This endpoint will post an answer to a specific question """
    data = request.json
    qn_answer = data['answer']
    user_id = data['user_id']
   
    # all_answers_per_question1 = []
    if qn_answer != "" and user_id != "":
        for question in questions_list:
            if question.qn_id == questionId:
                answer = Answer(user_id, questionId, qn_answer)
                {questionId:answer.answer_per_question()}
                answers_list.append({questionId:answer.answer_per_question()})
                return jsonify(answers_list)                                                         
            else:
                message = {"message": "No question with that id"}
                return message["message"], 400                      
    else:
        message = {"message": "Please add an answer to the question"}
        return message["message"], 400


