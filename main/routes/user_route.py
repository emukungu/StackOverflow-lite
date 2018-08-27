from .baseRoutes import request, jsonify, json, status, app, User

users_list = []

@app.route('/api/v1/register', methods = ['POST'])
def register():
    """ This endpoint will register a user in the database list """
    if request.method == 'POST':        
        #data from the client
        data = request.json

        username= data['username']
        email = data['email']
        password= data['password']
        
        if username == "" or email == "" or password == "":
            return jsonify({"message":"Fill in all the fields"}), 400
        #create an object from it
        sql = """INSERT INTO Users(username, email, password, user_id)
             VALUES(%s) RETURNING vendor_id;"""
        user =  User(username, email, password)
        # store the object in a list
        users_list.append(user)
        return jsonify({"message":"You have been successfully registered."}), 201


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