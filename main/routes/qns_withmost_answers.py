from .baseRoutes import request, jsonify, json, status, Question, app, datetime, cur, conn

@app.route('/api/v1/questions/answers', methods= ['GET'])
def qns_withmost_answers():    
    """This endpoint will fetch questions with most answers """
    most_answers = []
    query = """SELECT questions.title, COUNT(answers.answer) AS answers
    FROM answers
    INNER JOIN questions
    ON answers.question_id = questions.question_id
    GROUP BY questions.title
    ORDER BY COUNT(answers.answer) DESC;""" 
    cur.execute(query)
    returned_totalcount_per_question = cur.fetchall()

    if not returned_totalcount_per_question:
        return jsonify({"message":"No questions exist."}), 404 

    for row in returned_totalcount_per_question:
        qns_with_most_answers = {
            "title": row[0],
            "counted_answers": row[1]
        }
        most_answers.append(qns_with_most_answers)
    
    return jsonify({"Results": most_answers}), 200
    
    
    
     
