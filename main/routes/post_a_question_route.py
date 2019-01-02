from .baseRoutes import request, jsonify, json, status, Question, datetime, app, cur, conn
from .login import jwt_required, get_jwt_identity, login


@app.route('/api/v1/questions', methods = ['POST'])
@jwt_required
def post_a_question():
    """This endpoint will post a question """
    if request.method == 'POST':
        try:
            current_user_id = get_jwt_identity()["user_id"]

            #data from the client  
            post_data = request.get_json()

            # empty json request

            if not post_data:
                return jsonify({"error":"Invalid inputs"}), 400

            title = post_data["title"]
            desc = post_data['description']
            post_date = datetime.utcnow()
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
                    return jsonify({"message":"Question already exists"}), 409          

            # posted_qun = Question(title, desc,post_date,user_id)
            new_question = "INSERT INTO questions (title, question_description, date_created, user_id) VALUES(%s, %s, %s, %s);"
            cur.execute(new_question, (title, desc, post_date, user_id))
            conn.commit()
            cur.execute(""" SELECT users.username, questions.title, questions.date_created, questions.question_id
                        FROM questions
                        INNER JOIN users
                        ON questions.user_id = users.user_id
                        WHERE questions.title = %s 
                        AND questions.question_description = %s 
                        AND questions.date_created = %s
                        AND questions.user_id = %s; """,
                        (title, desc, post_date, user_id))
            row = cur.fetchone()     
            print(row) 
            posted_qn = {
                "username":row[0],
                "title":row[1],
                "date_created":row[2].strftime("%Y-%m-%d %H:%M:%S"),
                "question_id":row[3]
            }  
            return jsonify({"Successful":"Your question has been added to database", "Results":posted_qn}), 201               

        except:
            return jsonify({"message":"Token is expired"}), 400 