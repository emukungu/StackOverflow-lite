from .baseRoutes import *

@app.route('/api/v1/questions', methods = ['POST'])
def post():
    """This endpoint will post a question """
    message = {"message":""}
    if request.method == 'POST':        
        #data from the client
        data = request.json
        title= data['title']
        desc = data['description']
        date= data['date']
        user_id = data['user_id']
        if title == "" or desc == "" or date == "":
            message["message"] = "Fill in all the fields "
            return message["message"], 400
        else:
            #create an object from it
            question =  Question(title, desc, user_id, date)
            # store the object in a list
            questions_list.append(question)
            message = {"message":"Your question has been posted"}

            return message["message"], 200               


