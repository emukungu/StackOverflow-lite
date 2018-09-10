from .baseRoutes import request, jsonify, status, app, Question, questions_list, cur, conn


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    all_questions = []
    query = "SELECT * FROM questions;" 
    cur.execute(query)
    returned_all_questions = cur.fetchall()

    if not returned_all_questions:
        return jsonify({"message":"No questions exist."}), 404 

    for row in returned_all_questions:
        # column order: qn_id[0], title[1],qn_desc[2], date[3], user_id[4]
        # model order: title, desc, user_id, date, qn_id
        question_object = Question(row[1], row[2], row[4], row[3], row[0])
        question_details = question_object.listed_question()
        all_questions.append(question_details)
    return jsonify({"Results": all_questions}), 200