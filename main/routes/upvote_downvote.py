from .baseRoutes import request, jsonify, json, status, app, cur, conn
from .login import jwt_required, get_jwt_identity, login


@app.route('/api/v1/answers/<int:answerId>/vote', methods = ['POST'])
@jwt_required
def vote(answerId):
    current_user_id  = get_jwt_identity()["user_id"]

    data = request.get_json()
    vote = data["vote"]
    
    upcurrent_vote = 1
    downcurrent_vote = 1

    cur.execute("SELECT answer FROM answers WHERE answer_id = %s; ", (answerId,))
    qn_answer_vote = cur.fetchone()

    if  not qn_answer_vote:
        return jsonify({"message": "The answer doesnot exist on this platform"}), 404
    else:
        if vote == "upvote":
            cur.execute("SELECT up_vote FROM votes WHERE answer_id = %s and user_id =%s",(answerId, current_user_id))
            current_vote = cur.fetchone() 
            if not current_vote:
                cur.execute("INSERT INTO votes (up_vote, user_id, answer_id) VALUES(%s, %s, %s);", (upcurrent_vote, current_user_id, answerId))
                conn.commit()
            else:
                return jsonify({"message":"Already voted"})
        elif vote == "downvote":
            cur.execute("SELECT down_vote FROM votes WHERE answer_id = %s and user_id =%s",(answerId, current_user_id))
            current_vote = cur.fetchone() 
            if not current_vote:
                cur.execute("INSERT INTO votes (down_vote, user_id, answer_id) VALUES(%s, %s, %s);", (downcurrent_vote, current_user_id, answerId))
                conn.commit()
            else:
                return jsonify({"message":"Already voted"})

        cur.execute("SELECT COUNT(votes.up_vote) AS upvotes FROM votes WHERE answer_id = %s;", (answerId,))
        upvotes = cur.fetchone()[0]
        cur.execute("SELECT COUNT(votes.down_vote) AS downvotes FROM votes WHERE answer_id = %s;", (answerId,))
        downvotes = cur.fetchone()[0]
        total = upvotes - downvotes   
        return jsonify({"total_votes":total}), 201