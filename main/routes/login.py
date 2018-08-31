from .baseRoutes import request, jsonify, json, status, app, User, cur, conn
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

signature = app.config["SECRET_KEY"] = "bootcamp"

# create decorator function that decodes token
jwt = JWTManager(app)

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
        return jsonify({"message":"User doesnot exist on this platform"}), 405
    
    current_user = User(returned_user[0][0], returned_user[0][1], returned_user[0][2], returned_user[0][3])
    
    auth_username = current_user.username
    auth_user_id = current_user.user_id

    token = create_access_token(identity = {"user_id": auth_user_id, "username":auth_username})
    results = { "message": username + " exists",
                "token": token,
                "user_id": auth_user_id
    }
    return jsonify(results), 200 


@app.route('/api/v1/login', methods = ['GET'])
def wrong_login_method():
    return jsonify({"message":"Please enter the correct URL method"}), 404


