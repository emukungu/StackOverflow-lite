from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date, cur, conn
# from login import login


@app.route('/api/v1/questions', methods = ['POST'])
def post():
    """This endpoint will post a question """
    if request.method == 'POST':

        #data from the client  
        post_data = request.get_json()

        # empty json request

        if not post_data:
            return jsonify({"error":"Invalid inputs"}), 400

        title= post_data["title"]
        desc = post_data['description']
        post_date = str(date.today())
        user_id = post_data['user_id']
        # question_id = post_data['question_id']

        # empty input fields
        if title == "" or desc == "" or user_id is None:
            return jsonify({"message":"Fill in the missing fields"}), 400

        if type(title) is not str or type(desc) is not str or type(user_id) is not int:
            return jsonify({"message":"Enter the correct values"}), 400   

        query = "SELECT title, question_description FROM questions WHERE title = %s AND question_description = %s;"
        cur.execute(query, (title, desc))
        existing_questions = cur.fetchall()
        for i in existing_questions:
            if i[0] == title and i[1] == desc:
                return jsonify({"message":"Question already exists"}), 400             

        new_question = "INSERT INTO questions (title, question_description, date_created, user_id) VALUES(%s, %s, %s, %s);"
        cur.execute(new_question, (title, desc, post_date, user_id))
        conn.commit()
        return jsonify({"Successful":"Your question has been added to database"}), 201               


