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
        else:
            cur.execute("SELECT * FROM answers WHERE question_id = %s", (questionId,))
            result = cur.fetchall()
            for row in specific_question:
                specific_qn_details = Question(row[1], row[2], row[4], row[3], row[0])
            return jsonify({"Question":specific_qn_details.title , "Answers":result}), 200
    
    elif request.method == 'POST':
        return jsonify({"message":"Please enter the correct URL method"}), 405
