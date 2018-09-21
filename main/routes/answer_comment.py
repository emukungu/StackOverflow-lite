from .baseRoutes import request, jsonify, json, status, app, Answer, cur,conn
from .login import jwt_required, get_jwt_identity, login

@app.route('/api/v1/answers/<int:answerId>/comment', methods= ['POST'])
@jwt_required
def comment(answerId):
    """This endpoint will add a comment to a specific answer """
    current_user_id = get_jwt_identity()["user_id"]
    data = request.get_json()

    if not data:
        return jsonify({"error":"Invalid inputs"}), 400

    answer_comment = data['comment']

    user_id = current_user_id     

    if type(answer_comment) is not str:
        return jsonify({"error":"Enter the correct values"}), 400  

    if answer_comment:
        cur.execute("SELECT answer_id FROM answers WHERE answer_id = %s;", (answerId,))
        answer_to_be_commented = cur.fetchone()

        if answer_to_be_commented[0] == answerId:
            cur.execute("SELECT comment FROM comments WHERE answer_id = %s;", (answerId,))
            repeated_comment = cur.fetchall()

            for row in repeated_comment:
                if row[0] == answer_comment:
                    return jsonify({"message":"Comment already exists"}), 400
                        
            cur.execute("INSERT INTO comments (comment, user_id) VALUES(%s, %s);", (answer_comment, user_id))
            conn.commit()
            return jsonify({"Successful":"Your comment has been added", "AnswerId":answerId}), 201
        return jsonify({"message": "Answer doesnot exist"}), 404

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/comments', methods= ['GET'])
def get_all_comments():
    """ This endpoint will reject returning all comments on the platform"""
    return jsonify({"message":"Please enter the correct URL method"}), 405