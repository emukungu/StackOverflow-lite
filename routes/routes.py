from web_app import app
from flask import request, jsonify, json, Response
from copy import deepcopy
from models.models import Question
# import flask_api as api
# from flask_api import status
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
            questions = {"title": question.title}  
            listed_questions.append(questions)
        return jsonify(listed_questions)
        
    
             
        