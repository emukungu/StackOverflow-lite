from .baseRoutes import request, jsonify, json, status, Question, app, date, cur, conn


@app.route('/api/v1/<int:userId>/questions', methods= ['GET'])
def user_questions(userId):
    """ This endpoint will get questions by a specific user"""

    user_questions = []
    cur.execute("SELECT * FROM questions WHERE user_id = %s;",(userId,))
    returned_user_questions = cur.fetchall()

    if not returned_user_questions:
        return jsonify({"message":"You have not posted any questions."}), 404 

    for row in returned_user_questions:
        # column order: qn_id[0], title[1],qn_desc[2], date[3], user_id[4]
        # model order: title, desc, user_id, date, qn_id
        question_object = Question(row[1], row[2], row[4], row[3], row[0])
        question_details = question_object.listed_question()
        user_questions.append(question_details)
    return jsonify({"Results": user_questions}), 200

