from .baseRoutes import request, jsonify, json, status, Question, app, date, cur, conn

@app.route('/api/v1/questions/answers', methods= ['GET'])
def qns_withmost_answers():    
    """This endpoint will fetch questions with most answers """
    
    query = """SELECT questions.title, COUNT(answers.answer) AS Answers
    FROM answers
    INNER JOIN questions
    ON answers.question_id == questions.question_id
    ORDER BY COUNT(answers.answer) DESC;""" 
    cur.execute(query)
    returned_totalcount_per_question = cur.fetchall()

    if not returned_totalcount_per_question:
        return jsonify({"message":"No questions exist."}), 404 

    return jsonify({"Results": returned_totalcount_per_question}), 200
    
    
    
     
