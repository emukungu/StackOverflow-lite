from .baseRoutes import request, jsonify, json, status, app, cur, conn
from .login import jwt_required, get_jwt_identity, login


@app.route('/api/v1/answers/<int:answerId>', methods = ['POST'])
@jwt_required
def vote(answerId):
    current_user_id  = get_jwt_identity()["user_id"]

    data = request.get_json()
    vote = data["vote"]
        
    cur.execute("SELECT answer FROM answers WHERE answer_id = %s; ", (answerId,))
    qn_answer_vote = cur.fetchone()

    if  not qn_answer_vote:
        return jsonify({"message": "The answer doesnot exist on this platform"}), 404
    else:
        if vote == "upvote":
            cur.execute("SELECT up_vote FROM votes WHERE answer_id = %s",(answerId,))
            current_vote = cur.fetchone()[0] 
            if current_vote is None:
                current_vote = 1
            else: 
                current_vote += 1            
            cur.execute("INSERT INTO votes (up_vote, user_id) VALUES(%s, %s);", (current_vote, current_user_id))
            conn.commit()
            cur.execute("SELECT COUNT(votes.up_vote) AS upvotes FROM votes")
            upvotes = cur.fetchone()[0]
        elif vote == "downvote":
            cur.execute("SELECT down_vote FROM votes WHERE answer_id = %s",(answerId,))
            current_vote = cur.fetchone()[0] 
            if current_vote is None:
                return jsonify({"message":"Can't vote below zero"})
            else: 
                current_vote += 1            
            cur.execute("INSERT INTO votes (down_vote, user_id) VALUES(%s, %s);", (current_vote, current_user_id))
            conn.commit()
            cur.execute("SELECT COUNT(votes.down_vote) AS downvotes FROM votes")
            downvotes = cur.fetchone()[0]
        total = upvotes - downvotes   
        return jsonify({"total votes":total})