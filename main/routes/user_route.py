from flask import request, jsonify, json
from ..models.user_model import User
from flask_api import status
from main import app

users_list = []

@app.route('/api/v1/register', methods = ['POST'])
def register():
    """ This endpoint will register a user in the database list """
    message = {"message":""}
    if request.method == 'POST':        
        #data from the client
        data = request.json
        username= data['username']
        email = data['email']
        password= data['password']
        if username == "" or email == "" or password == "":
            message["message"] = "Fill in all the fields "
            return message["message"], 400
        else:
            #create an object from it
            user =  User(username, email, password)
            # store the object in a list
            users_list.append(user)
            message = {"message":"You have been successfully registered."}

            return message["message"], 201

@app.route('/api/v1/users', methods = ['GET'])
def get_all_users():     
    """This endpoint will fetch all users """
    listed_users = []
    if users_list == []:
        message = {"message":"No questions exist on this platform"}
        return message["message"], 404
    else:
        for user in users_list:
        #return dictionary that can be jsonified easily
            users = user.useraccount()  
            listed_users.append(users)
        return jsonify(listed_users), 200