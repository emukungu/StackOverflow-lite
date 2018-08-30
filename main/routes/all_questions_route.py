from .baseRoutes import request, jsonify, status, app, Question, questions_list, cur, conn


@app.route('/api/v1/questions', methods = ['GET'])
def get_all_questions():     
    """This endpoint will fetch all questions """
    all_questions = []
    query = "SELECT * FROM questions;" 
    cur.execute(query)
    returned_all_questions = cur.fetchall()

    if not returned_all_questions:
        return jsonify({"message":"No questions exist."}) 

    for i in returned_all_questions:
        # column order: qn_id[0], title[1],qn_desc[2], date[3], user_id[4]
        # model order: title, desc, user_id, date, qn_id
        question_object = Question(i[1], i[2], i[4], i[3], i[0])
        print("title : " + question_object.title)
        print("user_id : " + str(question_object.user_id))
        print("qn_id : " + str(question_object.qn_id))
        print("desc : " + question_object.description)
        question_details = question_object.listed_question()
        all_questions.append(question_details)
    return jsonify({"Results": all_questions})