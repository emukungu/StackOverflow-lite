from .baseRoutes import request, jsonify, json, status, app, questions_list, cur, conn, Question

@app.route('/api/v1/questions/<int:questionId>', methods = ['GET', 'POST'])
def question_id(questionId):
    """This endpoint will fetch a specific question """

    if request.method == 'GET':
        query = "SELECT * FROM questions WHERE question_id = %s"
        cur.execute(query, (questionId,))
        specific_question = cur.fetchall()

        if not specific_question:
            return jsonify({"message": "The question doesnot exist on this platform"}), 404
        cur.execute("SELECT * FROM answers WHERE question_id = %s", (questionId,))
        result = cur.fetchall()
        for i in specific_question:
            specific_qn_details = Question(i[1], i[2], i[4], i[3], i[0])
        return jsonify({"Question":specific_qn_details.title , "Answers":result}), 200
    
    elif request.method == 'POST':
        return jsonify({"message":"Please enter the correct URL method"}), 404
