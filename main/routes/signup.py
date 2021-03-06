from .baseRoutes import request, jsonify, json, status, app, User, cur, conn


@app.route('/api/v1/auth/signup', methods = ['POST'])
def signup():
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
        try:
            query = "SELECT username, email FROM users WHERE username = %s AND email = %s"
            cur.execute(query, (username, email))
            existing_users = cur.fetchall()
            for i in existing_users:
                if i[0] == username and i[1] == email:
                    return jsonify({"message":"User already exists"}), 403                        

            #create an object from it
            new_user = "INSERT INTO users (username, email, user_password) VALUES(%s, %s, %s);"
            cur.execute(new_user, (username, email, password))
            conn.commit()        
            return jsonify({"message":"You have been successfully registered."}), 201
        except:
            return jsonify({"message":"Username or email already exists"}), 400



@app.route('/api/v1/auth/signup', methods = ['GET'])
def get_all_users():     
    return jsonify({"message":"Please enter the correct URL method"}), 405
    
    
    

