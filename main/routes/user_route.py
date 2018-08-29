from .baseRoutes import request, jsonify, json, status, app, User, cur, conn

users_list = []
@app.route('/api/v1/register', methods = ['POST'])
def register():
    """ This endpoint will register a user in the database list """
    if request.method == 'POST':        
        #data from the client
        data = request.get_json()

        username = data['username']
        email = data['email']
        password= data['password']
        
        if username == "" or email == "" or password == "":
            return jsonify({"message":"Fill in all the fields"}), 400

        if type(username) is not str or type(email) is not str or type(password) is not str:
            return jsonify({"message":"Enter the correct values"}), 400           

        #user already in db
        query = "SELECT username, email FROM users WHERE username = %s AND email = %s"
        cur.execute(query, (username, email))
        existing_users = cur.fetchall()
        for i in existing_users:
            if i[0] == username and i[1] == email:
                return jsonify({"message":"User already exists"}), 400        

        #create an object from it
        new_user = "INSERT INTO users (username, email, user_password) VALUES(%s, %s, %s);"
        cur.execute(new_user, (username, email, password))
        conn.commit()        
        return jsonify({"message":"You have been successfully registered."}), 201


@app.route('/api/v1/users', methods = ['GET'])
def get_all_users():     
    """This endpoint will fetch all users """
    query = "SELECT * FROM users;" 
    cur.execute(query)
    returned_all_users = cur.fetchall()
    if not returned_all_users:
        return jsonify({"message":"No users exist."}) 
    return jsonify({"message":"All users", "Results":returned_all_users}), 200
    
    

@app.route('/api/v1/login', methods = ['POST'])
def login():
    login_data = request.get_json()
    
    username = login_data["username"]
    login_password = login_data["password"]

    if username == "" or  login_password == "":
            return jsonify({"message":"Fill in all the fields"}), 400

    elif type(username) is not str or type(login_password) is not str:
            return jsonify({"message":"Enter the correct values"}), 400 

    #query database for user    
    query = "SELECT username, user_password, email, user_id FROM users WHERE username = %s AND user_password = %s;"
    cur.execute(query, (username, login_password))
    returned_user = cur.fetchall()

    if not returned_user:
        return jsonify({"message":"Wrong login credentials "}), 405
    current_user = User(returned_user[0][0], returned_user[0][1], returned_user[0][2])
    return jsonify({"message": username + " exists","Results":current_user.useraccount()}), 200