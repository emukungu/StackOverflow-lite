from .baseRoutes import request, jsonify, json, status, app, cur, conn, Question

@app.route('/api/v1/questions/<int:questionId>', methods = ['GET'])
def question_id(questionId):
    """This endpoint will fetch a specific question """
    if request.method == 'GET':
        query = "SELECT * FROM questions WHERE question_id = %s"
        cur.execute(query, (questionId,))
        specific_question = cur.fetchall()

        if not specific_question:
            return jsonify({"message": "The question doesnot exist on this platform"}), 404
        else:
            for row in specific_question:
                specific_qn_details = Question(row[1], row[2], row[4], row[3], row[0])
            returned_qn = {
                    "title": specific_qn_details.title,
                    "description": specific_qn_details.description,
                    "qn_id": specific_qn_details.qn_id
                }           
            return jsonify({"Question":returned_qn}), 200


@app.route('/api/v1/questions/<int:questionId>', methods = ['POST'])
def wrong_qn_id(questionId):
    return jsonify({"message":"Please enter the correct URL method"}), 405