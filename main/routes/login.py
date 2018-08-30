from .baseRoutes import request, jsonify, json, status, app, User, cur, conn
import jwt
from functools import wraps

signature = app.config["SECRET_KEY"] = "bootcamp"

# create decorator function that decodes token
def authentication_required(v):
    wraps(v)
    def decode_token(*args, **kwargs):
        # token =
        return v(*args, **kwargs)

    return decode_token

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
    query = "SELECT * FROM users WHERE username = %s AND user_password = %s;"
    cur.execute(query, (username, login_password))
    returned_user = cur.fetchall()

    if not returned_user:
        return jsonify({"message":"Wrong login credentials "}), 405
    
    current_user = User(returned_user[0][0], returned_user[0][1], returned_user[0][2])
    auth_username = current_user.username
    auth_user_id = current_user.user_id

    token = jwt.encode({"username":auth_username, "user_id":auth_user_id,}, signature)
    results = { "message": username + " exists",
                "token": token.decode('utf-8')
    }
    return jsonify(results), 200 


@app.route('/api/v1/login', methods = ['GET'])
def wrong_login_method():
    return jsonify({"message":"Please enter the correct URL method"}), 404