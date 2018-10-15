from .baseRoutes import request, jsonify, status, app, Question, cur, conn


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    all_questions = []
    try:
        query = """ SELECT users.username, questions.title, questions.date_created, questions.question_id
                FROM questions
                INNER JOIN users
                ON questions.user_id = users.user_id
                ORDER BY questions.question_id DESC;"""
        cur.execute(query)
        returned_all_questions = cur.fetchall()

        for row in returned_all_questions:
            returned_object = {
            "username": row[0],
            "title": row[1],
            "date_created": row[2].strftime("%Y-%m-%d %H:%M:%S"),
            "qn_id": row[3]
            }    
            all_questions.append(returned_object)
        return jsonify({"Results": all_questions}), 200
    
    except:
        return jsonify({"message":"No questions exist."}), 404 

    