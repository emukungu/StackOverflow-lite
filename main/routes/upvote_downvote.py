from .baseRoutes import request, jsonify, json, status, app, cur, conn
from .login import jwt_required, get_jwt_identity, login

def voting(data):
    if data is None:
        data = 1
    else: 
        data += 1
    return data

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
            cur.execute("INSERT INTO comments (up_vote, user_id) VALUES(%s, %s);", (voting(current_vote), current_user_id))
            conn.commit()
            return jsonify({"message":"Up_voted", "Results": voting(current_vote)})
        elif vote == "downvote":
            cur.execute("SELECT down_vote FROM votes WHERE answer_id = %s",(answerId,))
            current_vote = cur.fetchone()[0]
            cur.execute("INSERT INTO answers (down_vote, user_id) VALUES(%s, %s);", (voting(current_vote), current_user_id))
            conn.commit()
        return jsonify({"message":"Down_voted", "Results": voting(current_vote)})
            
    