from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date, cur, conn
from .login import jwt_required, get_jwt_identity, login


@app.route('/api/v1/questions', methods = ['POST'])
@jwt_required
def post_a_question():
    """This endpoint will post a question """
    if request.method == 'POST':
        current_user_id = get_jwt_identity()["user_id"]

        #data from the client  
        post_data = request.get_json()

        # empty json request

        if not post_data:
            return jsonify({"error":"Invalid inputs"}), 400

        title= post_data["title"]
        desc = post_data['description']
        post_date = str(date.today())
        user_id = current_user_id
        
        # empty input fields
        if title == "" or desc == "" or user_id is None:
            return jsonify({"message":"Fill in the missing fields"}), 400

        if type(title) is not str or type(desc) is not str:
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


