from web_app import app
from flask import request, jsonify, json
from copy import deepcopy
from models.models import Question
from flask_api import status

questions_list = []

@app.route('/api/v1/questions', methods = ['POST'])
def post():
    """This endpoint will post a question """
    message = {"message":""}
    if request.method == 'POST':        
        #data from the client
        data = request.json
        title= data['title']
        desc = data['description']
        user_id= data['user_id']
        date= data['date']
        qn_answer = data['answer']
        if title == "" or desc == "" or user_id == "" or date == "" or qn_answer == "":
            message["message"] = "Fill in all the fields "
            return message["message"]     
        else:
            #create an object from it
            question =  Question(title, desc, user_id, date, qn_answer)
            # store the object in a list
            questions_list.append(question)
            message = {"message":"Your question has been posted"}
            return message["message"], status.HTTP_200_OK

@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    listed_questions = []
    if questions_list == []:
        message = {"message":"No questions exist on this platform"}
        return message["message"]
    else:
        for question in questions_list:
        #return dictionary that can be jsonified easily
            questions = {"title": question.title,
                         "qn_id":question.qn_id}  
            listed_questions.append(questions)
        return jsonify(listed_questions)
        
@app.route('/api/v1/questions/<int:questionId>', methods = ['GET'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    for question in questions_list:
        if question.qn_id == questionId:
            question_details = question.questionAccount()        
            return jsonify(question_details)        
        else:
            message = {"message": "The question doesnot exist on this platform"}
            return message["message"]    
             
        