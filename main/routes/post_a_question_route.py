from .baseRoutes import request, jsonify, json, status, Question, app, questions_list, date
from ..db import another_connection
cur = another_connection()

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

        elif type(title) is not str or type(desc) is not str or type(user_id) is not int:
            return jsonify({"message":"Enter the correct values"}), 400
            

        if type(title) is not str or type(desc) is not str or type(user_id) is not int:
            return jsonify({"message":"Enter the correct values"}), 400

        for question in questions_list:
            if title == question.title and desc == question.description :
                return jsonify({"message":"Question already exists"}), 400
                

        #create an object from it
    #     cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    #  (100, "abc'def"))
        new_question = "INSERT INTO question (title, question_description, date_created, user_id) VALUES(%s, %s, %s, %s)"
        cur.execute(new_question, (title, desc, post_date, user_id))
        # conn.commit()

        # question =  Question(title, desc, user_id, post_date)


        # store the object in a list

        # questions_list.append(question)
        # return jsonify({"Successful":"Your question has been posted"}), 201               


