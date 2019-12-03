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
                    return jsonify({"message":"Comment already exists"}), 409
                        
            cur.execute("INSERT INTO comments (comment, user_id, answer_id) VALUES(%s, %s, %s);", (answer_comment, user_id, answerId))
            conn.commit()
            cur.execute(""" SELECT users.username, comments.comment, comments.answer_id
                    FROM comments
                    INNER JOIN users
                    ON comments.user_id = users.user_id
                    WHERE comments.comment = %s 
                    AND comments.answer_id = %s 
                    AND comments.user_id = %s; """,
                    (answer_comment, answerId, user_id))
            queried_comment = cur.fetchone()
            posted_comment = {
                    "username":queried_comment[0],
                    "comment":queried_comment[1],
                    "ans_id":queried_comment[2]
                }
            return jsonify({"Successful":"Your comment has been added", "result":posted_comment}), 201
        return jsonify({"message": "Answer doesnot exist"}), 404

    return jsonify({"message": "Fill in all the fields"}), 400


@app.route('/api/v1/answers/<int:answerId>/comment', methods= ['GET'])
def get_all_comments(answerId):
    """ This endpoint will reject returning all comments on the platform"""
    all_comments = []
    try: 
        cur.execute("""SELECT users.username, comments.comment, comments.answer_id
                FROM comments
                INNER JOIN users
                ON comments.user_id = users.user_id
                WHERE comments.answer_id = %s;""", (answerId,))
        returned_all_comments = cur.fetchall()

        for row in returned_all_comments:                          
            returned_comments = {
                "commenting_user": row[0],
                "comment":row[1],
                "ans_id":row[2]
            }
            all_comments.append(returned_comments)
        return jsonify({"Results": all_comments}), 200

    except:
        return jsonify({"message":"No comments exist for the question."}), 404